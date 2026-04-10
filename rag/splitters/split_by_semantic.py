"""
语义分块器

优点：可以保证每个切片的语义一致
缺点：速度慢
"""

from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import (
    SemanticSplitterNodeParser,
)
from llama_index.core.node_parser.text import SentenceSplitter

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from dotenv import load_dotenv
import re

load_dotenv()

documents = SimpleDirectoryReader(
    input_files=["assets/shanxi/云冈石窟.txt"]
).load_data()


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


# 创建语义分块器
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-zh-v1.5")
splitter = SemanticSplitterNodeParser(
    # buffer_size=1,  # 缓冲区大小
    # breakpoint_percentile_threshold=90,  # 断点百分位阈值
    sentence_splitter=zh_sentence_splitter,  # 覆盖默认英文句子分割器
    embed_model=embed_model,  # 使用的嵌入模型
)

# 语义分块后再做长度控制（近似按字符规模）
char_limiter = SentenceSplitter(
    chunk_size=500,
    chunk_overlap=50,
)
# 创建基础句子分块器（作为对照）
# base_splitter = SentenceSplitter(
#     # chunk_size=512
# )


# 使用语义分块器对文档进行分块
semantic_nodes = splitter.get_nodes_from_documents(documents)
chunks = [node.get_content() for node in semantic_nodes]

with open("output/shanxi_yungang_semantic_chunks.txt", "w") as f:
    for chunk in chunks:
        f.write(chunk + f"\n\n{"-" * 10}\n\n")


# 使用基础句子分块器对文档进行分块
# base_nodes = base_splitter.get_nodes_from_documents(documents)
# print("\n=== 基础句子分块结果 ===")
# print(f"基础句子分块器生成的块数：{len(base_nodes)}")
# for i, node in enumerate(base_nodes, 1):
#     print(f"\n--- 第 {i} 个句子块 ---")
#     print(f"内容:\n{node.get_content()}")
#     print("-" * 50)
