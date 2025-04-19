# Integración de Ollama + Deepseek con Python + Fastapi

Este proyecto proporciona una API REST construida con FastAPI que se conecta a un modelo local de IA (deepseek-r1) gestionado por Ollama. Permite enviar consultas en lenguaje natural y recibir respuestas generadas por el modelo.

## ⛏Prerrequisitos

- Python 3.13 instalado y accesible en $PATH para facilitar el uso de Python desde la terminal [Descargar Python 3.13](https://www.python.org/downloads/release/python-3130/)
- Ollama instalado y funcionando en localhost [Descargar Ollama](https://ollama.com/download)
- Modelo `deepseek-r1` descargado con Ollama
  ```shell
  ollama pull deepseek-r1
  ```
- Postman instalado y crear una cuenta gratuita para acceder a todas las funcionalidades de la herramienta [Descargar Postman](https://www.postman.com/downloads/)

## 🚀Comenzar

- Ir a https://ollama.com
- Instalar Ollama en el sistema
- Extraer modelo deepseek-r1
- Sírvelo como servidor en el puerto: `11434`
- Ir a `https://github.com/ollama/ollama?tab=readme-ov-file`


## 📂Estructura del proyecto
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

## ⚙Instalación

Clonar el repositorio

```shell
git clone semana0_rafael_callata
cd semana0_rafael_callata
```

Abra su terminal y cree un entorno virtual con el siguiente comando.
```shell
python3 -m venv ./.venv
.\env\Scr\activate            # Windows (CMD/Powershell)
#source ./env/bin/activate    # macOS / Linux
```

A continuación, instale los siguientes paquetes y dependencias para el correcto funcionamiento del proyecto.
```shell
pip install --no-cache-dir -r requirements.txt
```
Configurar variables de entorno, cree un achivo `.env` con los siguientes variables dentro del archivo:
```shell
OLLAMA_HOST=http://127.0.0.1
OLLAMA_PORT=11434
OLLAMA_MODEL=deepseek‑r1
```

Verificar el modelo Ollama este funcionando correctamente en tu sistema operativo
```shell
ollama list
# debe aparecer: deepseek‑r1
```

## ▶Ejecutar API
Para ejecutar la aplicación en modo desarrollo con autoreload, escriba el siguiente comando.
```shell
uvicorn app.main:app --reload --host=<host> --port=<port>
```
Por ejemplo,
```shell
uvicorn server:app --reload --host=127.0.0.1 --port=8000
```
A continuación, visite: `http://127.0.0.1:8000/docs`

### Endpoints

- GET /
  - Descripción: Verifica el estado de la API.
  - Respuesta: { "status": "ok" }
- POST /preguntar
  - Descripción: Envía una pregunta al modelo.
  - Body (JSON):
    ```shell
    {
      "prompt": "¿Cuál es la capital de Francia?",
      "stream": false,
      "temperature": 0.7,
      "max_tokens": 512
    }
    ```
  - Respuesta (JSON):
    ```shell
    { "respuesta": "París" }
    ```

## 🛠Prueba del API
Antes de probar el paquete de instalación de la API con el siguiente comando.requests
```shell
pip install requests
```
### Pruebas con Postman
1. Importa o crea una colección en Postman.

2. Configura una solicitud POST http://localhost:8000/preguntar.

3. En el Body, selecciona raw JSON y pega un ejemplo de payload.

4. Envía la petición y verifica la respuesta.

5. Exporta la colección con capturas de los resultados.
El usuario preguntó:
```shell
{
  "prompt": "¿Cuál es la capital de Francia?"
}
```
Respuesta de salida de la API:
```shell
{
    "respuesta":"{\"model\":\"deepseek-r1\",\"created_at\":\"2025-04-19T02:28:48.5405089Z\",\"response\":\"\<think\>\\n\\n\</think\>\\n\\nLa capital de Francia es París.\",\"done\":true,\"done_reason\":\"stop\",\"context\":[151644,30182,44819,19003,1531,1187,6722,409,9694,685,30,151645,151648,271,151649,271,8747,6722,409,9694,685,1531,4270,23422,13],\"total_duration\":3763040100,\"load_duration\":19288200,\"prompt_eval_count\":13,\"prompt_eval_duration\":260436600,\"eval_count\":14,\"eval_duration\":3482755300}"
}
```
## 🔍Investigación

**1. ¿Qué es Ollama?**

   Ollama es una herramienta de línea de comandos que facilita la descarga y ejecución de modelos de inteligencia artificial localmente. Proporciona una API REST (por defecto en el puerto 11434) para enviar prompts y recibir respuestas sin necesidad de servicios en la nube.
   
**2. ¿Qué es FastAPI?**
   
   FastAPI es un framework moderno de Python para construir APIs web de alto rendimiento. Se basa en Starlette y Pydantic, ofrece validación automática de datos, generación de documentación OpenAPI (Swagger) y un rendimiento cercano al de Node.js o Go.
   
**3. ¿Qué es el modelo deepseek-r1?**

   Deepseek-r1 es un modelo de lenguaje optimizado para tareas de procesamiento de texto. Está diseñado para equilibrar precisión y eficiencia, permitiendo implementaciones locales con recursos moderados.
   
**4. Uso de peticiones con stream=True**

   Al habilitar stream=True, la API de Ollama envía fragmentos de la respuesta a medida que se generan. Esto permite construir interfaces interactivas o pipelines más responsivos, mostrando tokens en tiempo real.
      
**5. ¿Cómo garantizar la escalabilidad de una API que consume modelos de IA pesados?**
   
   - Desplegar múltiples réplicas de Ollama y balancearlas con un proxy (NGINX, Traefik).
   - Implementar colas de trabajo (RabbitMQ, Redis) para encolar peticiones.
   - Usar caching en nivel de petición (Redis) para respuestas repetidas.
   - Limitar concurrencia y tiempo de ejecución con semáforos o middleware.

**6. ¿Qué parámetros de Ollama (ej: num_ctx, temperature) afectan el rendimiento/calidad de respuestas?**
   
   - **temperature:** controla la aleatoriedad; valores más bajos generan respuestas más deterministas.
   - **max_tokens:** define la longitud máxima de la respuesta.
   - **num_ctx o context_size:** ajusta cuántos tokens del prompt se retienen en memoria, afectando latencia y uso de RAM.
     
**7. ¿Qué estrategias usar para balancear carga entre múltiples instancias de Ollama?**
   
   - Usar un balanceador HTTP (NGINX, HAProxy) que distribuya peticiones round-robin.
   - Implementar un gateway que monitorice la salud y carga de cada instancia.
   - Autoescalar instancias Docker/Kubernetes según métricas de CPU/latencia.
  
**8. ¿Qué patrones de diseño (ej: CQRS, Singleton) son útiles para integrar modelos de IA en backend?**
    
  - **Singleton:** para que la configuración de cliente HTTP o conexión a Ollama se inicialice una sola vez.
  - **Factory:** para crear servicios de IA que puedan apuntar a distintos modelos o proveedores.
  - **CQRS (Command Query Responsibility Segregation):** separar rutas de lectura (predicciones) y escritura (registro de uso) para optimizar y escalar cada parte.

