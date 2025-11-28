from google import genai
from dotenv import load_dotenv
import os
from pydantic import BaseModel
load_dotenv()

class Quiz(BaseModel):
    question: str
    options: list[str]
    answer: str

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="generate a quiz question on AI",
    config={
        "response_mime_type": "application/json",
        "response_json_schema": Quiz.model_json_schema(),
    }
)

print(response.text)
ai_quiz = Quiz.model_validate_json(response.text)

print(f'Question: {ai_quiz.question}, \n\n\n Options: \n\t -| {"\n\t -| ".join(ai_quiz.options)}, \n\n\n Answer: {ai_quiz.answer}')
