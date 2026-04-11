from langchain_community.document_loaders import WebBaseLoader
import bs4
import os
from markdownify import markdownify as md

os.environ["USER_AGENT"] = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
)

URL = "https://zh.wikipedia.org/wiki/%E9%BB%91%E7%A5%9E%E8%AF%9D%EF%BC%9A%E6%82%9F%E7%A9%BA"


def load_wukong_wiki_text():
    """加载维基百科黑神话：悟空页面，返回文本内容"""
    loader = WebBaseLoader(
        web_path=URL,
        bs_kwargs={"parse_only": bs4.SoupStrainer(id="bodyContent")},
    )
    docs = loader.load()
    return docs[0].page_content.strip()


def load_wukong_wiki_markdown():
    """加载维基百科黑神话：悟空页面，返回markdown内容"""
    loader = WebBaseLoader(
        web_path=URL,
        bs_kwargs={"parse_only": bs4.SoupStrainer(id="bodyContent")},
    )
    soup = loader.scrape()
    html = soup.prettify()
    markdown_content = md(html)
    return markdown_content


if __name__ == "__main__":
    # markdown_content = load_wukong_wiki_markdown()
    text_content = load_wukong_wiki_text()

    with open("assets/wukong/wukong_wiki.txt", "w") as f:
        f.write(text_content)
