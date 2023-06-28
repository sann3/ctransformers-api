from typing import List

from pydantic import BaseModel


class Message(BaseModel):
    role: str
    content: str


class Choice(BaseModel):
    index: int = 0
    finish_reason: str = "stop"
    message: Message


class Usage(BaseModel):
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0


class Response(BaseModel):
    id: str
    object: str = "messages"
    created: int
    model: str
    choices: List[Choice]
    usage: Usage