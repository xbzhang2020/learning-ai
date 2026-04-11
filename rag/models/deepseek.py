from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
import os

load_dotenv()

deepseek_model = ChatDeepSeek(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)
