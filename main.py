from scrap.scrap import get_articles, request
from config import KEYWORDS, BASE_URL


print(get_articles(BASE_URL, request(BASE_URL)))
