"""
使用窗口解析器处理文档，提高检索效果。
"""
from llama_index.core import Settings, Document, VectorStoreIndex
from llama_index.core.node_parser import SentenceWindowNodeParser, SentenceSplitter
from llama_index.core.postprocessor import MetadataReplacementPostProcessor
from llama_index.llms.deepseek import DeepSeek
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from dotenv import load_dotenv
import os


load_dotenv()

# 配置全局设置
Settings.llm = DeepSeek(
    model="deepseek-chat", temperature=0.1, api_key=os.getenv("DEEPSEEK_API_KEY")
)
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-zh-v1.5")
Settings.text_splitter = SentenceSplitter(
    separator="\n", chunk_size=50, chunk_overlap=0
)


# 使用窗口解析器处理文档
node_parser = SentenceWindowNodeParser.from_defaults(
    window_size=3,
    window_metadata_key="window",
    original_text_metadata_key="original_text",
)

# 基础的句子分块，用于对比
text_splitter = Settings.text_splitter

# 准备文档
with open("assets/wukong/玩法.txt", "r", encoding="utf-8") as f:
    game_knowledge = f.read()
documents = [Document(text=game_knowledge)]

# 创建节点
nodes = node_parser.get_nodes_from_documents(documents)
base_nodes = text_splitter.get_nodes_from_documents(documents)

# 创建索引
sentence_index = VectorStoreIndex(nodes)
base_index = VectorStoreIndex(base_nodes)

# 创建查询引擎
window_query_engine = sentence_index.as_query_engine(
    similarity_top_k=2,
    # the target key defaults to `window` to match the node_parser's default
    node_postprocessors=[
        MetadataReplacementPostProcessor(target_metadata_key="window")
    ],
)
base_query_engine = base_index.as_query_engine(similarity_top_k=2)


# 测试问答
question = "游戏中悟空有哪些形态变化？"
print("=== 使用窗口解析器的检索结果 ===")
print(f"\n问题：{question}")
window_response = window_query_engine.query(question)
print(f"回答：{window_response}")

# 展示检索到的原始句子和窗口内容
print("\n检索详情：")
for node in window_response.source_nodes:
    print(f"原始句子：{node.node.metadata['original_text']}")
    print(f"上下文窗口：{node.node.metadata['window']}")
    print("---")

print("\n=== 使用基础解析器的检索结果（对比）===")
print(f"\n问题：{question}")
base_response = base_query_engine.query(question)
print(f"回答：{base_response}")
