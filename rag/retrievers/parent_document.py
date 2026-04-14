"""
使用父文档检索器处理文档，提高检索效果。
"""
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.storage import InMemoryStore
from langchain_classic.retrievers import ParentDocumentRetriever
from langchain_core.documents import Document
from rag.embeddings.bge_small_zh import embeddings

# 父文本分块器
parent_splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000, 
    add_start_index=True,
    chunk_overlap=200,
    separators=["\n\n", "\n", "。", "！", "？", "；", ",", " ", ""]
)
# 子文本分块器
child_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400, 
    add_start_index=True,
    chunk_overlap=50,
    separators=["\n\n", "\n", "。", "！", "？", "；", ",", " ", ""]
)

# 创建向量存储，存储子文本
vectorstore = Chroma(embedding_function=embeddings)
# 创建存储层，存储父文本
store = InMemoryStore()

# 创建检索器
retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=store,
    child_splitter=child_splitter,
    parent_splitter=parent_splitter,
)

if __name__ == "__main__":
    with open("assets/wukong/玩法.txt", "r", encoding="utf-8") as f:
        game_knowledge = f.read()
    
    documents = [Document(page_content=game_knowledge)]

    # 添加文档
    retriever.add_documents(documents)

    # 检索文档
    results = retriever.invoke("游戏的玩法")
    for result in results:
        print(result.page_content)
        print("-" * 10)