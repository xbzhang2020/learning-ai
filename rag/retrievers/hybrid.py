"""
使用混合检索器检索文档。这里使用了 BM25 和向量检索，并进行了加权融合。
"""

from langchain_core.vectorstores import InMemoryVectorStore
from rag.embeddings.bge_small_zh import embeddings
from langchain_core.documents import Document
from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers import EnsembleRetriever

docs = [
    "The cat, commonly referred to as the domestic cat or house cat, is a small domesticated carnivorous mammal.",
    "The dog is a domesticated descendant of the wolf.",
    "Humans are the most common and widespread species of primate, and the last surviving species of the genus Homo.",
    "The scientific name Felis catus was proposed by Carl Linnaeus in 1758",
]


if __name__ == "__main__":
    queries = [
        "What is the scientifc name for cats",
    ]
    top_k = 2

    # BM25 检索器
    bm25_retriever = BM25Retriever.from_texts(docs)
    bm25_retriever.k = top_k

    # 向量存储检索器
    vector_store = InMemoryVectorStore(embedding=embeddings)
    vector_store.add_documents(
        documents=[Document(page_content=doc) for doc in docs],
        ids=[f"id_{i}" for i in range(len(docs))],
    )
    vector_store_retriever = vector_store.as_retriever(search_kwargs={"k": top_k})

    # 混合检索器
    ensemble_retriever = EnsembleRetriever(
        retrievers=[bm25_retriever, vector_store_retriever],
        weights=[0.5, 0.5],
    )

    for query in queries:
        print(f"\nQuery: {query}")

        bm25_results = bm25_retriever.invoke(query)[:top_k]
        vector_results = vector_store_retriever.invoke(query)[:top_k]
        hybrid_results = ensemble_retriever.invoke(query)[:top_k]

        print("\nBM25 Top Results:")
        for i, result in enumerate(bm25_results, start=1):
            print(f"{i}. {result.page_content}")

        print("\nVector Top Results:")
        for i, result in enumerate(vector_results, start=1):
            print(f"{i}. {result.page_content}")

        print("\nHybrid Top Results:")
        for i, result in enumerate(hybrid_results, start=1):
            print(f"{i}. {result.page_content}")

        print("\n" + "=" * 50)
