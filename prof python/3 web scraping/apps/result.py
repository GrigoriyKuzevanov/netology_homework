from .data import BASE_URL


def get_result(article):

    date_pub = article.find('time').attrs['title']
    title = article.find(class_='tm-article-snippet__title-link').find('span').text
    href_article = BASE_URL + article.find(class_='tm-article-snippet__title-link').attrs['href']
    return f'{date_pub} {title} {href_article}'
