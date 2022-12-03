from apps.articles import get_articles
from apps.preview import get_preview
from apps.fulltext import get_full_text
from apps.data import KEYWORDS
from apps.result import get_result


if __name__ == '__main__':
    articles = get_articles()
    for article in articles:
        prev = get_preview(article)
        text = get_full_text(article)
        for key in KEYWORDS:
            if key in prev or key in text:
                print(get_result(article))
                break
