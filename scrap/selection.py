import re
from config import KEYWORDS
from bs4 import BeautifulSoup


def get_pattern():
    pattern = ''
    for item in KEYWORDS:
        pattern += item+'|'
    return pattern[:-1]


def get_article_text(title, page):
    pattern = get_pattern()
    if page.status_code == 200:
        if len(re.findall(pattern, title.lower())) == 0:
            soup = BeautifulSoup(page.content, 'html.parser')
            p = soup.find(
                'div', xmlns="http://www.w3.org/1999/xhtml").text.lower()
            if len(re.findall(pattern[:-1], p)) == 0:
                pass
            else:
                print(f'{title} : {page.url}')
        else:
            print(f'{title} : {page.url}')
