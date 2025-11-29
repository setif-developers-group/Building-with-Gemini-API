# https://ai.google.dev/gemini-api/docs/text-generation#system-instructions

from google import genai
from google.genai import types
import os


client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
response = client.models.generate_content(
    model="gemini-2.0-flash-lite",
    config=types.GenerateContentConfig(
        system_instruction="You are a pirate.",
    ),
    contents="hello, there!"
)

print(response.text)