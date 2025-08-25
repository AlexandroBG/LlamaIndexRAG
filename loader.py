import os
import requests
from llama_index.core import SimpleDirectoryReader

def download_pdf_if_needed():
    """
    Descarga el PDF si no existe en la carpeta 'data'.
    """
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)
    pdf_path = os.path.join(data_dir, "csit150215.pdf")
    if not os.path.exists(pdf_path):
        url = "https://aircconline.com/csit/papers/vol15/csit150215.pdf"
        r = requests.get(url)
        with open(pdf_path, "wb") as f:
            f.write(r.content)
        print("PDF descargado en:", pdf_path)
    return pdf_path

def load_documents(path="data"):
    """
    Carga los documentos usando LlamaIndex SimpleDirectoryReader.
    """
    download_pdf_if_needed()
    reader = SimpleDirectoryReader(input_dir=path)
    return reader.load_data()
