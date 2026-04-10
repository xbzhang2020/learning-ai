"""
爬取医院介绍网页内容，并保存为txt文件
"""

from langchain_community.document_loaders import WebBaseLoader
from bs4 import SoupStrainer

def load_html(url):
    loader = WebBaseLoader(
        url,
        bs_kwargs={"parse_only": SoupStrainer(class_="content-top")},
        # 关键：保留标签边界为换行，避免内容被拼成一整行
        bs_get_text_kwargs={"separator": "\n", "strip": True},
    )
    docs = loader.load()
    for doc in docs:
        content = doc.page_content.replace("\xa0", " ")
        # 压缩多余空行，但保留段落分隔
        content = "\n".join(line.strip() for line in content.splitlines() if line.strip())
        doc.page_content = content
    return docs

if __name__ == "__main__":
    hospital_id = "571"
    hospital_url = f"https://www.yslw.com/hospital/{hospital_id}.html"
    docs = load_html(hospital_url)

    if len(docs) > 0:
        # print(docs[0].metadata)
        # print(docs[0].page_content)
        with open(f"assets/hospital/hospital_{hospital_id}.txt", "w") as f:
            f.write(docs[0].page_content.strip())
