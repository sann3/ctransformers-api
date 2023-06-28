import uuid
from datetime import datetime, timezone

from request import Request
from response import Response, Choice, Message, Usage


def create_choice(role: str, content: str) -> Choice:
    return Choice(message=Message(role=role, content=content))


def calculate_usage(request: Request, choices: [Choice]) -> Usage:
    len_list = [len(x.content) for x in request.messages]
    prompt_tokens = sum(len_list)

    len_list = [len(x.message.content) for x in choices]
    completion_tokens = sum(len_list)

    return Usage(prompt_tokens=prompt_tokens, completion_tokens=completion_tokens,
                 total_tokens=prompt_tokens + completion_tokens)


def create_response_from(request: Request, choices: [Choice]) -> 'Response':

    epoch = int(datetime.timestamp(datetime.now(timezone.utc)))
    return Response(id=str(uuid.uuid1()), created=epoch, model=request.model, choices=choices, usage=calculate_usage(request, choices))
