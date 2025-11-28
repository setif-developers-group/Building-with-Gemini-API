from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils import chat as  chat_utils
from schema import ChatHistory, Message 

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/chat")
async def chat(request: ChatHistory)-> Message:
    response = await chat_utils(request)
    return Message(role="model", message=response)


