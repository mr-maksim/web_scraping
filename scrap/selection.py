import re
from config import KEYWORDS
from bs4 import BeautifulSoup


def get_article_text(title, page):
    
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        p = soup.find('div', class_="article-formatted-body article-formatted-body article-formatted-body_version-2").find(
            'div', xmlns="http://www.w3.org/1999/xhtml").text
