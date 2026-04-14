"""
使用 BM25 检索器检索文档。
"""
from langchain_community.retrievers import BM25Retriever

retriever = BM25Retriever.from_texts(["foo", "bar", "world", "hello", "foo bar"])

from langchain_core.documents import Document

retriever = BM25Retriever.from_documents(
    [
        Document(page_content="foo"),
        Document(page_content="bar"),
        Document(page_content="world"),
        Document(page_content="hello"),
        Document(page_content="foo bar"),
    ]
)

result = retriever.invoke("which document contains 'foo'?")
for doc in result:
    print(doc.page_content)