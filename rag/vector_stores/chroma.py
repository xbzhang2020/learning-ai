from langchain_chroma import Chroma
from rag.embeddings.bge_small_zh import embeddings

chroma_wukong_db = Chroma(
    embedding_function=embeddings,
    persist_directory="chroma_wukong_db",
)
