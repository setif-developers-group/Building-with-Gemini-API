from google import genai
from google.genai import types
from decouple import config
import json

# Mock function
def get_weather_broadcast_next_6h(location: str):
    """
    Gets the weather broadcast for the next 6 hours for a given location.
    """
    # Mock data
    return {
        "location": location,
        "forecast": [
            {"time": "Now", "temperature": "15C", "condition": "Cloudy"},
            {"time": "+2h", "temperature": "14C", "condition": "Rain"},
            {"time": "+4h", "temperature": "12C", "condition": "Heavy Rain"},
            {"time": "+6h", "temperature": "11C", "condition": "Windy"},
        ]
    }

# Function declaration
weather_broadcast_function = {
    "name": "get_weather_broadcast_next_6h",
    "description": "Gets the weather broadcast for the next 6 hours for a given location to help decide what to wear.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

# Initialize client
GEMINI_API_KEY = config("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

tools = types.Tool(function_declarations=[weather_broadcast_function])
model_config = types.GenerateContentConfig(
    tools=[tools],
    system_instruction="You are a helpful assistant that recommends what to wear based on the weather. Use the get_weather_broadcast_next_6h function to get weather data."
)

def generate_response(user_message: str, history: list):
    """
    Generates a response from Gemini, handling function calls.
    """
    
    # Convert history to Gemini format
    gemini_history = []
    for msg in history:
        gemini_history.append(types.Content(
            role=msg["role"],
            parts=[types.Part(text=msg["content"])]
        ))
    
    # Add current user message
    # We don't add it to history list passed to API because we send it as 'contents'
    # But for multi-turn chat with function calling, we might need a chat session or manage history manually.
    # The simplest way with the client is to just pass the full history + new message.
    
    # Actually, let's use the chat feature if possible, or just append to contents.
    # The user example used `client.models.generate_content`.
    
    contents = gemini_history + [types.Content(role="user", parts=[types.Part(text=user_message)])]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents,
        config=model_config,
    )

    # Check for function call
    if response.candidates[0].content.parts[0].function_call:
        function_call = response.candidates[0].content.parts[0].function_call
        fn_name = function_call.name
        fn_args = function_call.args
        
        if fn_name == "get_weather_broadcast_next_6h":
            print(f"Calling function: {fn_name} with args: {fn_args}")
            result = get_weather_broadcast_next_6h(**fn_args)
            
            # Send result back to model
            # We need to construct the response parts
            # The model expects the function call result
            
            # We need to append the model's function call message and the function response to history
            contents.append(response.candidates[0].content)
            
            contents.append(types.Content(
                role="function",
                parts=[types.Part(
                    function_response=types.FunctionResponse(
                        name=fn_name,
                        response=result
                    )
                )]
            ))
            
            # Generate final response
            final_response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=contents,
                config=model_config # Keep config? Usually yes.
            )
            return final_response.text
            
    return response.text
