# для парсинга страниц
from bs4 import BeautifulSoup
# для запросов к сайту, получеия содержимого веб-стр
import requests
from requests import get
import time
import random

url= 'https://www.avito.ru/volgograd/avtomobili/daewoo/matiz-ASgBAgICAkTgtg2AmCjitg2~qig?cd=1&p=1&radius=300'
car_matiz = []
count_page = 1
while count_page <= 100:
    url = 'https://www.avito.ru/volgograd/avtomobili/daewoo/matiz-ASgBAgICAkTgtg2AmCjitg2~qig?cd=1&p=' + str(count_page) + '&radius=300'
    # print(url)
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    car_data = html_soup.find_all('div', class_="iva-item-body-KLUuy")

    if car_data != ():
        car_matiz.extend(car_data)
        value = random.random()
        scaled_value = 1 + (value * (9 - 5))
        print(scaled_value)
        time.sleep(scaled_value)
        print(html_soup)
        print('not_empty')
    else:
        print('empty')
        break
    count_page += 1

print(len(car_matiz))
print()
n = int(len(car_matiz)) - 1
count = 0
while count <= n:
    info = car_matiz[int(count)]
    # price = info.find('span', {"class": "price-text-_YGDY"}).text
    # title = info.find('h3', {"class": "title-root-zZCwT"}).text
    # print(title, ' ', price)
    ss = info.find('a', 'href').text
    print(ss)
    count += 1
