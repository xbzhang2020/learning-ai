from rag.vector_stores.chroma import chroma_wukong_db
from rag.models.deepseek import deepseek_model
from langchain_core.prompts import ChatPromptTemplate

if __name__ == "__main__":
    # 检索相似文档
    query = "游戏的玩法"
    similar_docs = chroma_wukong_db.similarity_search(query=query, k=3)
    similar_docs_text = "\n".join([doc.page_content for doc in similar_docs])
    print(similar_docs_text)
    print("-" * 10)

    # 构建提示词
    template = ChatPromptTemplate(
        [
            (
                "system",
                """你是一名游戏《黑神话：悟空》的专家，请根据以下文档回答用户的问题。如果用户的问题不在文档中，请回答“我不知道”。
                上下文：{context}""",
            ),
            ("human", "{query}"),
        ]
    )
    prompt = template.format(query=query, context=similar_docs_text)
    # response = model.invoke(prompt)
    # print(response.content)

    for chunk in deepseek_model.stream(prompt):
        print(chunk.text, end="")
    print("")