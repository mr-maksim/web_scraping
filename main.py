from scrap.scrap import get_articles, request
from scrap.selection import get_article_text
from config import BASE_URL
from tqdm import tqdm

if __name__ == '__main__':
    list = get_articles(BASE_URL, request(BASE_URL))
    for item in list:
        get_article_text(item[1], request(item[2]))
