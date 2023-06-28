from ctransformers import AutoModelForCausalLM
from fastapi import FastAPI

from builder import create_response_from
from request import Request
from response import Choice, Message

app = FastAPI()


def create_choice(index: int, role: str, content: str) -> Choice:
    return Choice(index=index,message=Message(role=role, content=content))


def inference(index: int, request: str, role: str):
    llm = AutoModelForCausalLM.from_pretrained('rustformers/redpajama-ggml',
                                               model_file='RedPajama-INCITE-Base-3B-v1-q4_0.bin',
                                               model_type="gpt_neox")
    llm_response = llm(request)
    return create_choice(index, role, llm_response)


@app.post("/inference")
async def get(request: Request):
    llm_response = [inference(i, x.content, x.role) for i, x in enumerate(request.messages)]
    return create_response_from(request, llm_response)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
