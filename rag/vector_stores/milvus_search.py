from rag.vector_stores.milvus import milvus_wukong_db

if __name__ == "__main__":
    results = milvus_wukong_db.similarity_search(
        "景区门票",
        k=3,
    )

    for result in results:
        print(result.metadata)
        print(result.page_content)
        print("-" * 10)
