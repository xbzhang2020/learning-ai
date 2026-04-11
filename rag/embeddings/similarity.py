from langchain_huggingface.embeddings import HuggingFaceEmbeddings
import numpy as np
from bge_small_zh import embeddings
from dotenv import load_dotenv

load_dotenv()


def cosine_similarity(vec1, vec2):
    dot = np.dot(vec1, vec2)
    return dot / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


if __name__ == "__main__":
    query_text = "今天天气怎么样？"
    query_embedding = embeddings.embed_query(query_text)

    document_text_list = [
        "今天天气很好，适合出门。",
        "今天我吃了北京烤鸭。",
        "今天我很生气",
    ]
    document_embedding_list = [
        embeddings.embed_query(text) for text in document_text_list
    ]

    for document_embedding in document_embedding_list:
        similarity = cosine_similarity(query_embedding, document_embedding)
        print("Cosine Similarity:", similarity)

    # Cosine Similarity: 0.7289771938339588
    # Cosine Similarity: 0.4192835022236361
    # Cosine Similarity: 0.6745224697886465
