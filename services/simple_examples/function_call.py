from google import genai
from google.genai import types
from decouple import config

# Load API key from environment variable
GEMINI_API_KEY = config("GEMINI_API_KEY")

# --- 1. Function Implementation ---
def add(a, b):
    """Adds two numbers."""
    return a + b

# --- 2. Function Declaration (Schema for the Model) ---
add_function_declaration = genai.types.FunctionDeclaration(
    name='add',
    description='Add two numbers',
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            'a': genai.types.Schema(type=genai.types.Type.NUMBER),
            'b': genai.types.Schema(type=genai.types.Type.NUMBER),
        },
        required=['a', 'b'],
    ),
)

# --- 3. Client and Configuration Setup ---
client = genai.Client(api_key=GEMINI_API_KEY)
model = "gemini-2.5-flash"

# Use the plural 'function_declarations'
tools = types.Tool(function_declarations=[add_function_declaration])

# Use genai.ToolsConfig and genai.FunctionCallingConfig for configuration
config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_budget=0),
    system_instruction = "You are a helpful assistant.",
    tools=[tools],
)

# --- 4. First API Call: Requesting the operation ---
prompt = "What is 2+2?"
response = client.models.generate_content(
    model=model,
    config=config,
    contents=prompt,
)

# --- 5. Handle Function Call or Direct Text Response ---
if response.candidates and response.candidates[0].content.parts[0].function_call:
    function_call = response.candidates[0].content.parts[0].function_call
    print(f"Function to call: {function_call.name}")
    print(f"Arguments: {function_call.args}")
    
    contents = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    
    if function_call.name == "add":
        # Execute the function
        result = add(function_call.args['a'], function_call.args['b'])
        print(f"Result: {result}")
        
        # Create function response part
        function_response_part = genai.types.Part.from_function_response(
            name=function_call.name,
            response={"result": result},
        )
        
        # Build conversation history for the second call
        contents.append(types.Content(
            role="model", 
            parts=[response.candidates[0].content.parts[0]] # Just the part with the function_call
        ))
        contents.append(types.Content(role="user", parts=[function_response_part]))
        
        # Configuration for the second call (no tools needed)
        second_config = genai.types.GenerateContentConfig(
            thinking_config=genai.types.ThinkingConfig(thinking_budget=0),
            system_instruction = "You are a helpful assistant.",
        )
        
        # --- 6. Second API Call: Sending result back for final answer ---
        response = client.models.generate_content(
            model=model,
            config=second_config,
            contents=contents,
        )
        print(f"\nFinal Answer: {response.text}")
        
else:
    # If the model decided not to call a function
    print(response.text)