def get_preview(article):
    preview = article.find(class_='tm-article-snippet').text
    return preview
