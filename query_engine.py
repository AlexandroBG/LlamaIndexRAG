import time
import os
from datetime import datetime
from dotenv import load_dotenv
from llama_index.core import Settings
from llama_index.llms.gemini import Gemini

# Cargar variables de entorno
load_dotenv()

# Contador simple para evitar exceder límites
request_count = 0
last_request_time = 0

def create_query_engine(index):
    """
    Crea un motor de consultas sobre el índice usando Gemini como LLM.
    """
    # Usar la misma variable que en config.py
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("❌ Falta GEMINI_API_KEY en el archivo .env")

    # Configurar Gemini como LLM
    Settings.llm = Gemini(model="models/gemini-1.5-flash", api_key=gemini_api_key)

    return index.as_query_engine(
        similarity_top_k=3,  # Limita contexto para ahorrar tokens
        response_mode="compact"  # Respuesta más eficiente
    )

def ask_question(query_engine, question: str):
    """
    Consulta el índice con control de rate limiting para API gratuita.
    """
    global request_count, last_request_time
    current_time = time.time()

    # Si han pasado más de 60 segundos, resetea el contador
    if current_time - last_request_time > 60:
        request_count = 0

    # Control básico de rate limiting (máx 10 por minuto para estar seguros)
    if request_count >= 10 and current_time - last_request_time < 60:
        wait_time = 60 - (current_time - last_request_time)
        print(f"⏳ Esperando {wait_time:.1f}s para no exceder límites gratuitos...")
        time.sleep(wait_time)
        request_count = 0

    request_count += 1
    last_request_time = current_time
    print(f"🤖 Procesando pregunta (request #{request_count})...")

    try:
        response = query_engine.query(question)
        return str(response)
    except Exception as e:
        if "quota" in str(e).lower() or "limit" in str(e).lower():
            print("❌ Límite de API alcanzado. Espera un momento.")
            return "Error: Límite de API gratuita alcanzado. Intenta de nuevo en unos minutos."
        else:
            print(f"❌ Error: {e}")
            return f"Error al procesar la consulta: {e}"
