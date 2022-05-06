from bs4 import BeautifulSoup
import requests as rq


REQUEST_HEADERS = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
BASE_URL = 'https://habr.com'
    

if __name__ == '__main__':
    url = 'https://habr.com/ru/all/'
    page = rq.get(url, headers=REQUEST_HEADERS)
    if page.status_code != 200:
        print('No site')
        exit()
    
    keywords = input('Enter key words\n').lower().split()

    soup = BeautifulSoup(page.text, 'html.parser')
    articles = soup.find_all('article')
    
    for article in articles:
        print_flag = False
        time_pub = article.time['title']
        hubs = []
        for hub in article.find_all('span', class_='tm-article-snippet__hubs-item'):
            hubs.append(hub.span.text.lower())
        preview = article.find('div', class_='article-formatted-body').text.lower()
        for key in keywords:
            if key in hubs or key in preview:
                print_flag = True
                break
        if print_flag:
            print(f"{time_pub} - {article.h2.text}\n\tlink: {BASE_URL + article.h2.a['href']}")
