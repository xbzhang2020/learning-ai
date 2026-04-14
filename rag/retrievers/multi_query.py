"""
使用 LangChain 的 MultiQueryRetriever 生成多个查询语句，提高检索效果。
"""
import logging

from langchain_classic.retrievers import MultiQueryRetriever
from rag.models.deepseek import deepseek_model
from rag.vector_stores.chroma import chroma_wukong_db

logging.basicConfig()
logging.getLogger("langchain_classic.retrievers.multi_query").setLevel(logging.INFO)

retriever_from_llm = MultiQueryRetriever.from_llm(
    retriever=chroma_wukong_db.as_retriever(), llm=deepseek_model
)

docs = retriever_from_llm.invoke(
    "那个，我最近听说《黑神话：悟空》要发布了，很期待，能介绍一下吗？"
)

print('\n')
for doc in docs:
    print(doc.page_content)
    print("-" * 10)
