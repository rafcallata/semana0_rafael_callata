from pydantic_settings import BaseSettings, SettingsConfigDict

# Cargar variables de entorno desde el archivo .env
class Settings(BaseSettings):
    OLLAMA_HOST: str
    OLLAMA_PORT: int
    OLLAMA_MODEL: str

    # indicamos el .env y su encoding
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )
settings = Settings()