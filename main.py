from scrap.scrap import get_articles, request
from scrap.selection import get_article_text,get_pattern
from config import BASE_URL

if __name__ == '__main__':
    list = get_articles(BASE_URL, request(BASE_URL))
    print(f'{("*")*10} Слова для поиска : {get_pattern()} {("*")*10}')
    for item in list:
        get_article_text(item[1], request(item[2]))
