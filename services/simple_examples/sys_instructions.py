# https://ai.google.dev/gemini-api/docs/text-generation#system-instructions

from google import genai
import os


client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
response = client.chat(
    model="gemini-2.0-flash-lite",
    config={
        "system": "You are a pirate."
    },
    contents="hello, there!"
)

print(response.text)