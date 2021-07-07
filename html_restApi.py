import numpy as np
import pandas as pd
import operator
import json
from pprint import pprint
import xml.etree.ElementTree as ET
import xmljson
import requests
from bs4 import BeautifulSoup

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

    return result


print(get_actors('https://www.kinopoisk.ru/film/326/'))
