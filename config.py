import os
from dotenv import load_dotenv
import google.generativeai as genai

def configure_gemini():
    """
    Configura Gemini para generación de texto.
    """
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("No se encontró GEMINI_API_KEY en .env")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-pro")
