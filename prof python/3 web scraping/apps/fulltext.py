from .data import BASE_URL, HEADERS
import requests
import bs4


def get_full_text(article):

    href = article.find(class_='tm-article-snippet__title-link').attrs['href']
    url_article = BASE_URL + href
    response_article = requests.get(url_article, headers=HEADERS)
    info_article = response_article.text
    soup_for_full_article = bs4.BeautifulSoup(info_article, features='html.parser')
    full_text = soup_for_full_article.find(
        class_='article-formatted-body article-formatted-body article-formatted-body_version-2'
    )
    if full_text is None:
        full_text = soup_for_full_article.find(
            class_='article-formatted-body article-formatted-body article-formatted-body_version-1')
        res = full_text.text
    else:
        res = full_text.text
    return res
