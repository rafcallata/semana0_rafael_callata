# Integración de Ollama + Deepseek con Python + Fastapi

Este proyecto proporciona una API REST construida con FastAPI que se conecta a un modelo local de IA (deepseek-r1) gestionado por Ollama. Permite enviar consultas en lenguaje natural y recibir respuestas generadas por el modelo.

## Comenzar

- Ir a https://ollama.com
- Instalar Ollama en el sistema
- Extraer modelo deepseek-r1
- Sírvelo como servidor en el puerto: `11434`
- Ir a `https://github.com/ollama/ollama?tab=readme-ov-file`


## Estructura del proyecto
```bash
├── app/                   # Carpeta principal del código
    ├── main.py            # Archivo principal para ejecutar la aplicación
    ├── config.py          # Configuración y carga de .env
    ├── schemas.py         # Definición de modelos de datos (Pydantic)
    ├── exceptions.py      # Manejadores de errores personalizados
    └── services/
        └── ollama.py      # Lógica de comunicación con Ollama
├── .env                   # Archivo para gestionar variables de entorno
├── requirements.txt       # Archivo para las dependencias del proyecto
└── README.md              # Documento explicativo del proyecto
```

## Instalación

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
