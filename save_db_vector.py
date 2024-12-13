import os
from langchain_core.documents.base import Document
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import pickle
import faiss
from dotenv import load_dotenv
from multiprocessing import freeze_support




def load_vectorstore(vectorstore_dir: str):
    idx_faiss_path = os.path.join(vectorstore_dir, "index.faiss")
    print(f"FAISS path: {idx_faiss_path}")
    # Carrega o índice FAISS
    index = faiss.read_index(idx_faiss_path)
    print("FAISS index loaded")

    # Carrega os metadados do vetor
    idx_pkl_path = os.path.join(vectorstore_dir, "index.pkl")
    print(f"Pickle path: {idx_pkl_path}")

    with open(idx_pkl_path, "rb") as f:
        index_metadata = pickle.load(f)
    print(f'index_metadata loaded')
    print(index_metadata)

    # Retorna o vetor FAISS reconstruído
    loaded_vectorstore = FAISS.fro
    return FAISS(index, index_metadata['faiss_metadata'], index_metadata['index_to_id_map'], index_metadata['id_to_text_map'])




def read_pdf_docs(sourceFolderName: str):
    # Carregar documentos
    docs = []

    for file in os.listdir(sourceFolderName):
        filePath = os.path.join(sourceFolderName, file)
        loader = PyPDFLoader(filePath)
        docs.extend(loader.load())

    return docs


def split_documents(docs:list[Document]):
    # Divisão em pedaços de texto / Split
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    splits = text_splitter.split_documents(docs)
    return splits


def save_db_vector(splits: list[Document], saveFolderName: str):
    # Embeddings
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-m3")
    
    # Armazenamento
    vectorstore = FAISS.from_documents(splits, embeddings)
    dir_save_path = os.path.join(os.path.dirname(__file__), 'vectorstore', saveFolderName)
    vectorstore.save_local(dir_save_path)
    return vectorstore



if __name__ == '__main__':
    load_dotenv() 
    freeze_support()

    current_dir = os.path.dirname(__file__)
    saveFolderName = 'pdc_ccee' # Adicione aqui o que quer ler
    dir_src = os.path.join(current_dir, saveFolderName)

    docs = read_pdf_docs(dir_src)

    # Split retorna a lista de documentos porem com separação diferente da leitura bruta do PDF, pode ou nao ser interessante.
    splits = split_documents(docs)
    
    db = save_db_vector(splits=splits, saveFolderName=saveFolderName)
    print(f'Banco de dados salvo na pasta vector/{saveFolderName}')
 

