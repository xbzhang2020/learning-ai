"""
按照 Markdown 标题进行分块

优点：可以按照 Markdown 标题进行分块，适用于 Markdown 文档。
缺点：只能按照 Markdown 标题进行分块，无法按照其他规则进行分块。
"""

from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)

if __name__ == "__main__":
   
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]

    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on,
    )
   
    with open("assets/wukong/黑悟空版本介绍.md", "r", encoding="utf-8") as f:
        markdown_text = f.read()
    markdown_chunks = markdown_splitter.split_text(markdown_text)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20,
    )
    chunks = text_splitter.split_documents(markdown_chunks)

    with open("output/wukong_version_markdown_chunks.txt", "w") as f:
        for chunk in chunks:
            f.write(f"{str(chunk.metadata)}\n{chunk.page_content}\n\n{"-" * 10}\n\n")
