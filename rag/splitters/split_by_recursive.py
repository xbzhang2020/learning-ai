"""
按照递归字符进行分块

优点：可以设置多级分割符，保证句子完整性，适用于大多数场景。
缺点：不能保证每个切片的语义一致
"""

if __name__ == "__main__":
    from langchain_community.document_loaders import TextLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    loader = TextLoader("assets/shanxi/云冈石窟.txt")
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
    chunks = text_splitter.split_documents(docs)

    for chunk in chunks:
        print(chunk.metadata)
        print(chunk.page_content)
        print("-" * 10)
