from rag.splitters.split_by_recursive import split_by_recursive
from rag.vector_stores.chroma import chroma_wukong_db

if __name__ == "__main__":
    chunks = split_by_recursive("assets/wukong/wukong_wiki.txt")
    chroma_wukong_db.add_documents(chunks)
    print("Success")
