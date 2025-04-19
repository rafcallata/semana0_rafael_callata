from pydantic import BaseModel

class Pregunta(BaseModel):
    prompt: str
    stream: bool = False
    temperature: float = 0.7
    max_tokens: int = 512

class ErrorResponse(BaseModel):
    detail: str