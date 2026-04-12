from langchain_milvus import Milvus
from rag.embeddings.bge_small_zh import embeddings

URI = "./milvus_wukong.db"
ALIAS = "default"

milvus_wukong_db = Milvus(
    embedding_function=embeddings,
    connection_args={"uri": URI, "alias": ALIAS},
    index_params={"index_type": "FLAT", "metric_type": "L2"},
)
  