import requests
from config import KEYWORDS,BASE_URL

def get_status(url):
    page = requests.get(url)
    return page.status_code

get_status(BASE_URL)
