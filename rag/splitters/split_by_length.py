"""
按照固定长度进行分块

优点：速度快
缺点：尽管可以设置重叠度，但仍然可能会将一句话切分成两半，破坏句子完整性
"""

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter


if __name__ == "__main__":
    loader = TextLoader("assets/shanxi/云冈石窟.txt")
    docs = loader.load()

    text_splitters = CharacterTextSplitter(separator="", chunk_size=200, chunk_overlap=20)
    chunks = text_splitters.split_documents(docs)

    with open("output/shanxi_yungang_length_chunks.txt", "w") as f:
        for chunk in chunks:
            f.write(f"{str(chunk.metadata)}\n{chunk.page_content}\n\n{"-" * 10}\n\n")
