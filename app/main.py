import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.schemas import Pregunta, ErrorResponse
from app.services.ollama import OllamaService
from app.exceptions import http_exception_handler

app = FastAPI(
    title="API Ollama + Deepseek-r1",
    version="v1",
    description="Proyecto IA local con FastAPI y Ollama"
)

# CORS (en producción restringe origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Handler global de HTTPException
app.add_exception_handler(Exception, http_exception_handler)

# Dependency: una única instancia de servicio
def get_ollama_service() -> OllamaService:
    return OllamaService()

@app.get("/", tags=["health"])
async def health():
    return {"status": "ok"}

@app.post(
    "/preguntar",
    response_model=dict[str, str],
    responses={500: {"model": ErrorResponse}, 504: {"model": ErrorResponse}}
)
async def preguntar(
    req: Pregunta,
    svc: OllamaService = Depends(get_ollama_service)
):
    """
    Recibe JSON con los parámetros de la pregunta,
    delega en OllamaService y devuelve el texto crudo.
    """
    respuesta = await svc.generar(req)
    return {"respuesta": respuesta}

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )