from google import genai
import os


client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
response = client.chat(
    model="gemini-2.0-flash-lite",
    contents="Explain what is AI"
)

print(response)

# print(response.####)
