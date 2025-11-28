from pydantic import BaseModel
from typing import Literal

class Message(BaseModel):
    role: Literal["user", "model"]
    message: str

class ChatHistory(BaseModel):
    messages: list[Message]