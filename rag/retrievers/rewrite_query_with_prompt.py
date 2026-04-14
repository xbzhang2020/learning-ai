"""
使用提示词重写查询语句，提高检索效果。可以结合知识库结构约束查询重写的结果。
"""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

prompt = """
你是一个游戏专家，请将用户的问题重写为更准确的查询语句。

重写规则：
- 去除无关信息，保留核心内容，比如闲聊内容、语气词等
- 明确查询意图，比如是查询游戏玩法，还是查询游戏剧情，还是查询游戏角色等
- 将模糊的查询文同转换为具体的查询

输出格式：直接给出重写后的查询语句，不要添加任何其他内容

示例：
用户的问题：你好，我想知道《黑神话：悟空》的游戏玩法。
重写后的查询语句：游戏玩法

用户的问题：我想知道《黑神话：悟空》的游戏剧情。
重写后的查询语句：游戏剧情

用户的问题：我想知道《黑神话：悟空》的游戏角色。
重写后的查询语句：游戏角色
"""

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": "那个，我最近听说《黑神话：悟空》要发布了，很期待，能介绍一下吗？"},
    ],
    stream=False
)

print(response.choices[0].message.content)