"""
按照主题进行分块

优点：可以保证每个切片的主题一致
缺点：速度慢
"""

from rag.models.deepseek import deepseek_model
from langchain.agents import create_agent


system_prompt = """
你是一个游戏领域的知识库构建专家。请根据文档内容，将文档分割成多个主题，用于游戏咨询问答系统。

切片规则：
1. 每个切片应该只包含一个明确的主题，主题之间应该有明显的界限。
2. 每个切片的内容长度尽量不要超过 1000 个字符。
3. 严格基于文档内容，不要添加任何主观臆断。
4. 如果原文某片段内容不足以支撑一个主题，则忽略原文该片段内容，不要生成主题。

输出格式：使用 JSON 结构输出，每个切片包含以下字段：
- title: 主题标题
- content: 主题内容

示例输出：
[
    {
        "title": "游戏玩法",
        "content": "游戏玩法内容"
    },
    {
        "title": "游戏剧情",
        "content": "游戏剧情内容"
    },
    {
        "title": "游戏评价",
        "content": "游戏评价内容"
    }
]
"""

if __name__ == "__main__":
    doc_path = "assets/wukong/wukong_wiki.txt"
    with open(doc_path, "r") as f:
        doc = f.read()

    agent = create_agent(
        model=deepseek_model,
        system_prompt=system_prompt,
    )

    for event in agent.stream(
            {"messages": [{"role": "user", "content": doc}]},
            stream_mode="values",
        ):
            event["messages"][-1].pretty_print()
