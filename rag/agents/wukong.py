"""
wukong agent: 使用工具检索相关文档并回答用户的问题。
"""

from rag.vector_stores.chroma import chroma_wukong_db
from rag.models.deepseek import deepseek_model
from langchain.agents import create_agent
from langchain.tools import tool


@tool()
def retrieve_context(query: str):
    """Retrieve information to help answer a query."""
    retrieved_docs = chroma_wukong_db.similarity_search(query=query, k=2)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized


if __name__ == "__main__":
    prompt = "你是一名游戏《黑神话：悟空》的专家，请利用工具检索相关文档并回答用户的问题。如果用户的问题不在文档中，请回答“我不知道”。"
    agent = create_agent(
        model=deepseek_model,
        system_prompt=prompt,
        tools=[retrieve_context],
    )
    query = "游戏的玩法"
    messages = [{"role": "user", "content": query}]
    for event in agent.stream(
        {"messages": messages},
        stream_mode="values",
    ):
        event["messages"][-1].pretty_print()
