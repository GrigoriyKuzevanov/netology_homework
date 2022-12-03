import requests
import bs4

BASE_URL = 'https://habr.com'
url = BASE_URL + '/ru/all'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

HEADERS = {
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Cookie': '_ym_uid=16575186344791389; _ym_d=1657518634; _ym_isad=1; habr_web_home_feed=/all/; hl=ru; fl=ru; _ga=GA1.2.2138013028.1657518634; _gid=GA1.2.466607878.1657518634',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Windows',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=HEADERS)
info = response.text

soup = bs4.BeautifulSoup(info, features='html.parser')
articles = soup.find_all('article')

for article in articles:

    date_pub = article.find('time').attrs['title']
    title = article.find(class_='tm-article-snippet__title-link').find('span').text
    href_article = BASE_URL + article.find(class_='tm-article-snippet__title-link').attrs['href']

    preview = article.find(class_='tm-article-snippet').text

    href = article.find(class_='tm-article-snippet__title-link').attrs['href']
    url_article = BASE_URL + href
    response_article = requests.get(url_article, headers=HEADERS)
    info_article = response_article.text
    soup_for_full_article = bs4.BeautifulSoup(info_article, features='html.parser')
    full_text = soup_for_full_article.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')

    if full_text is None:
        full_text = soup_for_full_article.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-1')
        res = full_text.text
    else:
        res = full_text.text

    for key in KEYWORDS:
        if key in preview.lower() or key in res.lower():
            print(f'{date_pub} {title} {href_article}')
            break
