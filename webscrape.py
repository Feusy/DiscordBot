from bs4 import BeautifulSoup
import requests

# Get last news from Portfolió
def get_last_news():
    html_text = requests.get('https://www.portfolio.hu/frisshirek').text
    soup = BeautifulSoup(html_text, 'lxml')
    news_post = soup.find('div', class_='title')
    post = news_post.find('a').text
    link = 'https://www.portfolio.hu' + news_post.a['href']
    print(f'New post: {post}')
    print(f'See more: {link}')
    return 'Portfolió', post, link
