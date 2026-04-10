"""
语义分块器

优点：可以保证每个切片的语义一致
缺点：速度慢，无法精准控制切片长度
"""

from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import (
    SemanticSplitterNodeParser,
)

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from dotenv import load_dotenv
import re


def zh_sentence_splitter(text: str) -> list[str]:
    """
    中文友好的句子切分：
    1) 先按 \n 分段（当前数据中 \n 常作为段落边界）
    2) 再按中英文句末标点切句
    """
    rough_parts = [p.strip() for p in text.split("\n") if p.strip()]
    sentences: list[str] = []

    for part in rough_parts:
        split_part = re.split(r"(?<=[。！？!?；;])", part)
        split_part = [s.strip() for s in split_part if s.strip()]
        sentences.extend(split_part)

    return sentences if sentences else [text]


if __name__ == "__main__":
    load_dotenv()

    # 创建语义分块器
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-zh-v1.5")
    splitter = SemanticSplitterNodeParser(
        # buffer_size=1,  # 缓冲区大小
        # breakpoint_percentile_threshold=90,  # 断点百分位阈值
        sentence_splitter=zh_sentence_splitter,  # 覆盖默认英文句子分割器
        embed_model=embed_model,  # 使用的嵌入模型
    )

    # 使用语义分块器对文档进行分块
    documents = SimpleDirectoryReader(
        input_files=["assets/shanxi/云冈石窟.txt"]
    ).load_data()
    semantic_nodes = splitter.get_nodes_from_documents(documents)
    chunks = [node.get_content() for node in semantic_nodes]

    with open("output/shanxi_yungang_semantic_chunks.txt", "w") as f:
        for chunk in chunks:
            f.write(chunk + f"\n\n{"-" * 10}\n\n")
