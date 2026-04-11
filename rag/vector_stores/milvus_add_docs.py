from rag.splitters.split_by_recursive import split_by_recursive
from rag.vector_stores.milvus import milvus_wukong_db

if __name__ == "__main__":
    chunks = split_by_recursive("assets/shanxi/云冈石窟.txt")
    milvus_wukong_db.add_documents(chunks)
    print("Success")