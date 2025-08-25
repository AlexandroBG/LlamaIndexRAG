# 🤖 LlamaIndex RAG con Gemini

Sistema de Retrieval Augmented Generation (RAG) que utiliza **solo recursos gratuitos** para crear un chatbot inteligente que puede responder preguntas sobre documentos PDF.

## ✨ Características

- 🆓 **100% Gratuito**: Usa Gemini API gratuita y embeddings de HuggingFace
- 📄 **Procesamiento de PDFs**: Descarga y procesa automáticamente documentos
- 🔍 **Búsqueda Vectorial**: Índice vectorial para recuperación precisa de información
- ⚡ **Control de Rate Limiting**: Respeta los límites de la API gratuita
- 🛡️ **Manejo de Errores**: Control robusto de excepciones y límites de API

## 🏗️ Arquitectura

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   PDF Loader    │───▶│  Vector Index   │───▶│  Query Engine   │
│  (loader.py)    │    │  (indexer.py)   │    │(query_engine.py)│
└─────────────────┘    └─────────────────┘    └─────────────────┘
        │                       │                       │
        ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ SimpleDirectory │    │ HuggingFace     │    │ Gemini 1.5      │
│ Reader          │    │ Embeddings      │    │ Flash (FREE)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/LlamaIndexRAGV1.git
cd LlamaIndexRAGV1
```

### 2. Crear entorno virtual
```bash
python -m venv .alex
source .alex/bin/activate  # En macOS/Linux
# o
.alex\Scripts\activate     # En Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar API Key
Crea un archivo `.env` en la raíz del proyecto:
```bash
GEMINI_API_KEY=tu_api_key_aquí
```

**¿Cómo obtener tu API Key gratuita?**
1. Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Inicia sesión con tu cuenta de Google
3. Crea una nueva API Key
4. Copia y pega la key en tu archivo `.env`

## 📊 Límites de la API Gratuita

| Recurso | Límite Gratuito |
|---------|----------------|
| Requests | 15/minuto, 1,500/día |
| Tokens | 1M tokens/día |
| Embeddings | Ilimitado (local) |

## 🎯 Uso

### Ejecución básica
```bash
python main.py
```

### Estructura de archivos
```
LlamaIndexRAGV1/
├── .alex/              # Entorno virtual
├── data/               # PDFs (se crea automáticamente)
├── config.py           # Configuración de Gemini
├── loader.py           # Carga de documentos
├── indexer.py          # Construcción del índice
├── query_engine.py     # Motor de consultas
├── main.py             # Punto de entrada
├── requirements.txt    # Dependencias
├── .env               # Variables de entorno
└── README.md          # Este archivo
```

## 🔧 Componentes

### `config.py`
- Configuración de la API de Gemini
- Validación de variables de entorno
- Inicialización del modelo gratuito

### `loader.py`
- Descarga automática de PDFs
- Lectura de documentos con LlamaIndex
- Gestión de la carpeta `data/`

### `indexer.py`
- Construcción del índice vectorial
- Embeddings de HuggingFace (gratuitos)
- Fallback a embeddings por defecto

### `query_engine.py`
- Motor de consultas sobre el índice
- Control de rate limiting
- Manejo de errores de API

## 📝 Ejemplo de Uso

```python
from config import configure_gemini
from loader import load_documents
from indexer import build_index
from query_engine import create_query_engine, ask_question

# Configurar
model = configure_gemini()
documents = load_documents("data")
index = build_index(documents)
query_engine = create_query_engine(index)

# Consultar
response = ask_question(query_engine, "¿De qué trata este documento?")
print(response)
```

## 🛠️ Tecnologías Utilizadas

- **[LlamaIndex](https://www.llamaindex.ai/)**: Framework RAG
- **[Google Gemini](https://ai.google.dev/)**: LLM gratuito
- **[HuggingFace](https://huggingface.co/)**: Embeddings gratuitos
- **[Sentence Transformers](https://www.sbert.net/)**: Modelos de embeddings
- **[PyPDF](https://pypdf.readthedocs.io/)**: Procesamiento de PDFs

## 🤝 Contribuciones

Las contribuciones son bienvenidas! Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 🆘 Soporte

Si encuentras algún problema:

1. Revisa que tu API key esté configurada correctamente
2. Verifica que todas las dependencias estén instaladas
3. Abre un [issue](https://github.com/tu-usuario/LlamaIndexRAGV1/issues) describiendo el problema

## 🎯 Roadmap

- [ ] Interfaz web con Streamlit
- [ ] Soporte para múltiples formatos (Word, TXT, etc.)
- [ ] Cache de embeddings para mejor performance
- [ ] Integración con más LLMs gratuitos
- [ ] Modo conversacional con historial
