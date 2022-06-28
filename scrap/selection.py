import re
from config import KEYWORDS
from bs4 import BeautifulSoup
from debug_tools.logger import logger


@logger('logs')
def get_pattern():
    pattern = ''
    for item in KEYWORDS:
        pattern += item+'|'
    return pattern[:-1]


@logger('logs')
def get_article_text(title, page):
    pattern = get_pattern()
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        if len(re.findall(pattern, title.lower())) == 0:
            date = soup.find(
                'span', class_='tm-article-snippet__datetime-published').find('time')["title"].split(',')
            p = soup.find(
                'div', xmlns="http://www.w3.org/1999/xhtml").text.lower()
            if len(re.findall(pattern[:-1], p)) == 0:
                pass
            else:
                print(f'{date[0]} - {title} - {page.url}')
        else:
            date = soup.find(
                'span', class_='tm-article-snippet__datetime-published').find('time')["title"].split(',')
            print(f'{date[0]} - {title} - {page.url}')
