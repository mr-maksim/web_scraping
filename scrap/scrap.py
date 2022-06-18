import requests
from bs4 import BeautifulSoup


def request(url):
    page = requests.get(url)
    return page


def get_articles(url, page):
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        pages = soup.find_all('article', class_="tm-articles-list__item")
        for item in pages:
            title = item.find(
                'h2', class_='tm-article-snippet__title tm-article-snippet__title_h2').find('span')
            link = item.find('h2', class_='tm-article-snippet__title tm-article-snippet__title_h2').find(
                'a', class_='tm-article-snippet__title-link').get('href')
            return title, link
    else:
        return 'Page status code != 200'
