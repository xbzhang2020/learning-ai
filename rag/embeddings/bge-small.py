from langchain_huggingface.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True},
)

text = "今天天气怎么样？"
query_result = embeddings.embed_query(text)

print(len(query_result))
print(query_result[:3])
