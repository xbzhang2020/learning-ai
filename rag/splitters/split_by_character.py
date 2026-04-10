"""
按照固定字符进行分块

优点：可以设置分隔符，保证句子完整性
缺点：只能设置一种分割符，如果分割后内容超过切片长度，无法继续处理切片。
"""

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter


if __name__ == "__main__":
    loader = TextLoader("assets/shanxi/云冈石窟.txt")
    docs = loader.load()

    text_splitters = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
    chunks = text_splitters.split_documents(docs)

    with open("output/shanxi_yungang_character_chunks.txt", "w") as f:
        for chunk in chunks:
            f.write(f"{str(chunk.metadata)}\n{chunk.page_content}\n\n{"-" * 10}\n\n")
