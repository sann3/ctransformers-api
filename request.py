from typing import List

from pydantic import BaseModel


class Message(BaseModel):
    role: str
    content: str


class Request(BaseModel):
    model: str
    messages: List[Message]