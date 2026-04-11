from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
import os

load_dotenv()

deepseek_model = ChatDeepSeek(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)


# Please install OpenAI SDK first: `pip3 install openai`
# import os
# from dotenv import load_dotenv
# from openai import OpenAI

# load_dotenv()

# client = OpenAI(
#     api_key=os.getenv('DEEPSEEK_API_KEY'),
#     base_url="https://api.deepseek.com")

# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant"},
#         {"role": "user", "content": "Tell me a joke in Chinese"},
#     ],
#     stream=False
# )

# print(response.choices[0].message.content)
