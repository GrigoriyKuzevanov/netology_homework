import requests
from .data import BASE_URL, HEADERS
import bs4


def get_articles():
    url = BASE_URL + '/ru/all'
    response = requests.get(url, headers=HEADERS)
    text = response.text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('article')
    return articles
