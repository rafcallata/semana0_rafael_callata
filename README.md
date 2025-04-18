# Integración de Ollama + Deepseek con Python + Fastapi

## Empezar

- Ir a https://ollama.com
- Instalar Ollama en el sistema
- Extraer modelo deepseek-r1
- Sírvelo como servidor en el puerto: `11434`
- Ir a `https://github.com/ollama/ollama?tab=readme-ov-file`

## Installación

Abra su terminal y cree un entorno virtual con el siguiente comando.
```shell
python3 -m venv ./.venv
source ./.venv/bin/activate
```

A continuación, instale los siguientes paquetes uno por uno para fastapi.
```shell
pip install fastapi
pip install pydantic
pip install uvicorn
```
A continuación, instale el siguiente paquete para interactuar con `ollama`.
```shell
pip install ollama
```

## Ejecutar API
Para ejecutar la aplicación, escriba el siguiente comando.
```shell
uvicorn server:app --host=<host> --port=<port>
```
Por ejemplo,
```shell
uvicorn server:app --host=127.0.0.1 --port=8000
```
A continuación, visite: `http://127.0.0.1:8000/docs`

## API de prueba
Antes de probar el paquete de instalación de la API con el siguiente comando.requests
```shell
pip install requests
```
