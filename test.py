from bs4 import BeautifulSoup  # для парсинга старниц
import requests  # для запросов к сайту, получения содержимого веб-страницы
from requests import get
import time
import random

url = 'https://www.avito.ru/lipetsk/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&rn=25934&p='
houses = []
count = 1
while count <= 5:
    url = 'https://www.avito.ru/lipetsk/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1&rn=25934&p=' + str(
        count)
    print(url)
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    house_data = html_soup.find_all('div', class_="item__line")
    if house_data != []:
        houses.extend(house_data)
        value = random.random()
        scaled_value = 1 + (value * (9 - 5))
        print(scaled_value)
        time.sleep(scaled_value)
    else:
        print('empty')
        break
    count += 1

print(len(houses))
print(houses[0])
print()
n = int(len(houses)) - 1
count = 0
while count <= 5:  # count <= n
    info = houses[int(count)]
    price = info.find('span', {"class": "snippet-price"}).text
    title = info.find('a', {"class": "snippet-link"}).text
    print(title, ' ', price)
    count += 1