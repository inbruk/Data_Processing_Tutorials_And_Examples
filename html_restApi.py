import numpy as np
import pandas as pd
import operator
import json
from pprint import pprint
import xml.etree.ElementTree as ET
import xmljson
import requests
from bs4 import BeautifulSoup
from pprint import pprint

response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
# print(response.text)

currencies = response.json()
# pprint(currencies)
# pprint(currencies['Valute']['UAH'])
# print(currencies['Valute']['CZK']['Name'])

def exchange_rates(currency, format='full'):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url).json()['Valute']
    data = response[currency]
    if format == 'full':
        return data
    elif format == 'value':
        return data['Value']


#print(exchange_rates('UAH'))
#print(exchange_rates('UAH', format='full'))
#print(exchange_rates('UAH', format='value'))


def currency_name(ID):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    resp = requests.get(url).json()['Valute']
    for curr_k in resp:
        curr_v = resp[curr_k]
        if curr_v['ID'] == ID:
            return curr_v['Name']
    return ''


# print(currency_name('R01810'))


news_url = 'https://nplus1.ru/news/2019/06/04/slothbot'
response = requests.get(news_url)
# print(response.status_code)
# print(response.text)
page = BeautifulSoup(response.text, 'html.parser')
#print(page.title)
print(page.title.text)

print(page.find('h1').text)
print(page.find('time').text)


def wiki_header(url):
    response = requests.get(url)
    page = BeautifulSoup(response.text, 'html.parser')
    result =  page.find('h1').text
    return result


# print(wiki_header('https://en.wikipedia.org/wiki/Operating_system'))
# print(page.find('div', class_='body').text)

links = page.find_all('a')
# print(len(links))
# for link in links:
#    print(link.text)


all_blocks = page.find_all('div', class_='container')
# print(all_blocks)
first_block = all_blocks[0]
links = first_block.find_all('a')
# print([link.text for link in links[:10]])


def get_actors(url):
    response = requests.get(url)
    page = BeautifulSoup(response.text, 'html.parser')
    containers = page.find_all('ul', class_='styles_list__I97eu')

    result = []
    for curr_c in containers:
        actors = curr_c.find_all('a')
        for curr_a in actors:
            result.append(curr_a.text)
        result.append('...')

    return result


# print(get_actors('https://www.kinopoisk.ru/film/326/'))

# df = pd.read_html('https://www.cbr.ru/key-indicators/')[1]
df = pd.read_html('https://www.cbr.ru/key-indicators/')[0]
# print(df)


soup = BeautifulSoup(requests.get('https://www.cbr.ru/key-indicators/', headers={'User-Agent': 'Mozilla/5.0'}).text, 'html.parser')
all_blocks = soup.find_all('div', class_='key-indicator_content offset-md-2')
data = all_blocks[1].find('table')
df = pd.read_html(str(data))[0]
# print(df)


url = 'https://www.cbr.ru/key-indicators/'
# Таблица с драгметаллами оказалась второй по счёту
df1 = pd.read_html(url)[0]
# print(df1)
df2 = pd.read_html(url)[1]
# print(df2)


url = 'https://www.cbr.ru/key-indicators/'
soup = BeautifulSoup(requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text, 'html.parser')
# print(soup.text)

all_blocks = soup.find_all('div', class_='key-indicator_content offset-md-2')
# Данные таблицы с драгметаллами находятся во втором блоке
data = all_blocks[1].find('table')
# print(data)
df = pd.read_html(str(data))[0]
# print(df)


url = 'https://www.banki.ru/banks/ratings/'
soup = BeautifulSoup(requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text, 'html.parser')
all_blocks = soup.find_all('table', class_='standard-table standard-table--row-highlight margin-bottom-small margin-top-x-small')
data = all_blocks[0]
# print(data)
df = pd.read_html(str(data))[0]
# print(df)


url = 'https://api.vk.com/method/users.get'
token = '1dcca85c1dcca85c1dcca85c5b1db45d3911dcc1dcca85c7cd5b1da449992bd8dfe83cb'
# params = {'user_id': 1, 'v': 5.95, 'fields': 'sex,bdate', 'access_token':token, 'lang': 'ru'}
# response = requests.get(url, params=params)
# print(response.text)
# pprint(response.json())
# user = response.json()['response'][0]
# print(user['bdate'])
# print(user['first_name'])


# ids = ",".join(map(str, range(1, 501)))
# params = {'user_ids': ids, 'v': 5.95, 'fields': 'sex', 'access_token': token, 'lang': 'ru'}
# response = requests.get(url, params=params).json()
# resp_arr = response['response']
# value_arr = list(map(lambda x: x['sex'], resp_arr))
# print(len(value_arr))
# print(value_arr.count(0))
# print(value_arr.count(1))
# print(value_arr.count(2))
# print(round(value_arr.count(1)/(len(value_arr)-value_arr.count(0)),2))


# url = 'https://api.vk.com/method/groups.getMembers'
# params = {
#     'group_id': 'vk',
#     'v': 5.95,
#     'access_token': token
# }
# response = requests.get(url, params = params)
# data = response.json()
# print(data)
# offset = 0
# user_ids = []
# max_count = 100000
# count = 1000
# while offset < max_count:
#     params = {
#         'group_id': 'vk',
#         'v': 5.95,
#         'count': count,
#         'offset': offset,
#         'access_token': token
#     }
#     r = requests.get(url, params=params)
#     data = r.json()
#     user_ids += data['response']['items']
#     offset += count
#
# print(len(user_ids))
# print(user_ids[99999])


def get_smm_index(group_name, token):
    url = 'https://api.vk.com/method/wall.get'
    params = {
        'domain': 'vk',
        'filter': 'owner',
        'count': 10,
        'offset': 0,
        'access_token': token,
        'v': 5.95
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data)


get_smm_index('', token)
