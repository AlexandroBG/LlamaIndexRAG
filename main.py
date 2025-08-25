from config import configure_gemini
from loader import load_documents
from indexer import build_index
from query_engine import create_query_engine, ask_question

def main():
    print("🚀 Iniciando RAG con Gemini GRATUITO + LlamaIndex")
    print("=" * 50)

    # Configurar Gemini (solo tier gratuito)
    model = configure_gemini()

    # Cargar documentos (descarga automática del PDF si no existe)
    print("\n📄 Cargando documentos...")
    documents = load_documents("data")
    print(f"✅ Documentos cargados: {len(documents)}")

    # Construir índice con embeddings HuggingFace (gratis y local)
    print("\n🔍 Construyendo índice vectorial...")
    index = build_index(documents)
    print("✅ Índice construido")

    # Crear motor de consultas
    print("\n⚙️ Configurando motor de consultas...")
    query_engine = create_query_engine(index)
    print("✅ Motor de consultas listo")

    # Consultas de ejemplo
    questions = [
        "What is LangChain?",
        "What are the main components mentioned in the document?",
        "Summarize the key points of this paper"
    ]

    print("\n" + "=" * 50)
    print("🤖 CONSULTAS DE EJEMPLO")
    print("=" * 50)

    for i, question in enumerate(questions, 1):
        print(f"\n📝 Pregunta {i}: {question}")
        print("-" * 40)
        response = ask_question(query_engine, question)
        print(f"🤖 Respuesta: {response}\n")

        # Pausa entre preguntas para no saturar la API gratuita
        if i < len(questions):
            print("⏳ Pausa de 2 segundos...")
            import time
            time.sleep(2)

    print("\n" + "=" * 50)
    print("✅ Demo completada usando solo recursos GRATUITOS")
    print("💡 Gemini: API gratuita")
    print("💡 Embeddings: HuggingFace local (gratis)")
    print("💡 LlamaIndex: Open source")

if __name__ == "__main__":
    main()
