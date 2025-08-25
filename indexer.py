from llama_index.core import VectorStoreIndex

def build_index(documents):
    """
    Construye un índice vectorial usando embeddings por defecto.
    """
    try:
        # Intenta usar embeddings de HuggingFace
        from llama_index.embeddings.huggingface import HuggingFaceEmbedding
        from llama_index.core import Settings

        embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
        Settings.embed_model = embed_model
        print("Usando HuggingFace embeddings")

    except ImportError:
        print("Usando embeddings por defecto de OpenAI")
        # Usar embeddings por defecto si HuggingFace no está disponible
        pass

    return VectorStoreIndex.from_documents(documents)
