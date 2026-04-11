"""
按照递归字符进行分块

优点：可以设置多级分割符，保证句子完整性，适用于大多数场景。
缺点：不能保证每个切片的语义一致
"""

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_by_recursive(file_path: str, chunk_size: int = 200, chunk_overlap: int = 20):
    loader = TextLoader(file_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    chunks = text_splitter.split_documents(docs)
    return chunks


if __name__ == "__main__":

    chunks = split_by_recursive("assets/shanxi/云冈石窟.txt")

    with open("output/shanxi_yungang_recursive_chunks.txt", "w") as f:
        for chunk in chunks:
            f.write(f"{str(chunk.metadata)}\n{chunk.page_content}\n\n{"-" * 10}\n\n")
