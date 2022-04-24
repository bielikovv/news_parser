import sqlite3
import requests
from bs4 import BeautifulSoup



def parse_url(url, tag, clas):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    items = soup.find_all(tag, class_=clas)
    return items


def add_to_db(news, title_of_table):
    for el in news:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        cursor.execute(f"""
            INSERT INTO '{title_of_table}' (time, title, link)
            VALUES (?, ?, ?)
        """, (el['time'], el['title'], el['link']))
        connection.commit()


#PRAVDA
for item in parse_url('https://www.pravda.com.ua/rus/news/', 'div', 'article_news_list article_news_bold'):
    news = []
    news.append({
        'time': item.find('div', class_='article_time').get_text(),
        'title': item.find('div', class_='article_content').get_text(),
        'link': item.find('a').get('href'),
    })

    for el in news:
        if not el['link'].startswith('https://'):
            el['link'] = 'https://www.pravda.com.ua' + el['link']
    add_to_db(news, 'news_pravdasite')



#NV
for item in parse_url('https://nv.ua/', 'div', 'feed-item'):
    news = []
    news.append({
        'time': item.find('div', class_='feed-item-additional-pub-date').get_text(),
        'title': item.find('a').get_text(),
        'link': item.find('a').get('href'),
    })

    add_to_db(news, 'news_nvsite')

