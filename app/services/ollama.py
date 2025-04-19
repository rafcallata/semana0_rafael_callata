import json
import httpx
from fastapi import HTTPException

from app.config import settings
from app.schemas import Pregunta

class OllamaService:
    def __init__(self):
        self.base_url = f"{settings.OLLAMA_HOST}:{settings.OLLAMA_PORT}/api"
        self.model = settings.OLLAMA_MODEL
        self._client = httpx.AsyncClient(timeout=60.0)

    async def generar(self, req: Pregunta) -> str:
        payload = {
            "prompt": req.prompt,
            "stream": req.stream,
            "temperature": req.temperature,
            "max_tokens": req.max_tokens,
            "model": self.model,
        }
        resp = await self._client.post(f"{self.base_url}/generate", json=payload)
        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code, detail=resp.text)
        return resp.text
