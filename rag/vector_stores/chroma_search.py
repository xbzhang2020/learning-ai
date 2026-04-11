from rag.vector_stores.chroma import chroma_wukong_db

if __name__ == "__main__":
    results = chroma_wukong_db.similarity_search(
        "景区门票",
        k=3,
    )

    for result in results:
        print(result.metadata)
        print(result.page_content)
        print("-" * 10)
