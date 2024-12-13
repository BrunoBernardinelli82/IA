from save_db_vector import load_vectorstore
import os

current_dir = os.path.dirname(__file__)

# Carrega o vectorstore salvo
saveFolderName = 'db_faiss'
vectorstore_path = os.path.join(current_dir, 'vectorstore', saveFolderName)
print(vectorstore_path)

vectorstore = load_vectorstore(vectorstore_path)

# Usa a função as_retriever para criar um retriever
retriever = vectorstore.as_retriever(
    search_type='mmr',
    search_kwargs={'k': 3, 'fetch_k': 4}
)


# Agora você pode usar o retriever para buscar documentos
query = "Qual capital minimo do agente comercializador?"
results = retriever.retrieve(query)

# Exibindo os resultados
for result in results:
    print(result)

