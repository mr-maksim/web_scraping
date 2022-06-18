import requests
from bs4 import BeautifulSoup


def request(url):
    page = requests.get(url)
    return page


def get_articles(url, page):
    list = []
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        pages = soup.find_all('article', class_="tm-articles-list__item")
        for id, item in enumerate(pages):
            title = item.find(
                'h2', class_='tm-article-snippet__title tm-article-snippet__title_h2').find('span').text
            link = item.find('h2', class_='tm-article-snippet__title tm-article-snippet__title_h2').find(
                'a', class_='tm-article-snippet__title-link').get('href')
            list.append([id+1, title, f'https://habr.com{link}'])
        return list
    else:
        return 'Page status code != 200'
