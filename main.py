import re
from bs4 import BeautifulSoup
import requests as rq


if __name__ == '__main__':
    url = 'https://habr.com/ru/all/'
    page = rq.get(url)
    print(page)
    if page.status_code != 200:
        print('No site')
        exit()
    soup = BeautifulSoup(page.text, 'html.parser')
    articles = soup.find_all('article')
    print(articles)
    for article in articles:
        hubs = article.find_all('span', class_='tm-article-snippet__hubs-item')
        print(hubs)
        print(article.h2.a['href'])
        print(article.br)
        break
