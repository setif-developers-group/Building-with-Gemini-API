# https://ai.google.dev/gemini-api/docs/text-generation

from google import genai
import os

# this is the wrong way to do it 
client = genai.Client(api_key="GOOGLE_API_KEY")
response = client.chat(
    model="gemini-2.0-flash-lite",
    contents="Explain what is AI"
)

print(response)

# print(response.####)
