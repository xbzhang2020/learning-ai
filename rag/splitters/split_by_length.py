"""
按照固定长度进行分块

优点：速度快
缺点：尽管可以设置重叠度，但仍然可能会将一句话切分成两半，破坏句子完整性
"""

from langchain_text_splitters import CharacterTextSplitter
from rag.loaders.load_web import load_wukong_wiki_docs

def split_wukong_wiki_docs_by_length():
    docs = load_wukong_wiki_docs()
    text_splitters = CharacterTextSplitter(
        separator="", chunk_size=1000, chunk_overlap=20
    )
    chunks = text_splitters.split_documents(docs)
    return chunks

if __name__ == "__main__":
    chunks = split_wukong_wiki_docs_by_length()

    for chunk in chunks[:5]:
        print(chunk.metadata)
        print(chunk.page_content)
        print("-" * 10)
