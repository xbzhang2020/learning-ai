from langchain_huggingface.embeddings import HuggingFaceEmbeddings
import numpy as np

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True},
)


def cosine_similarity(vec1, vec2):
    dot = np.dot(vec1, vec2)
    return dot / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


query_text = "今天天气怎么样？"
query_embedding = embeddings.embed_query(query_text)

document_text_list = [
    "今天天气很好，适合出门。",
    "今天我吃了北京烤鸭。",
    "今天我很生气",
]
document_embedding_list = [embeddings.embed_query(text) for text in document_text_list]

for document_embedding in document_embedding_list:
    similarity = cosine_similarity(query_embedding, document_embedding)
    print("相似度:", similarity)

# 相似度: 0.7289771938339588
# 相似度: 0.4192835022236361
# 相似度: 0.6745224697886465