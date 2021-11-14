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
import datetime
import time
import schedule
import re

# url = 'https://kudago.com/public-api/v1.4/events/'
# params = '?order_by=-publication_date&page_size=100&location=msk&fields=id,title,dates,description,price,site_url'
# response = requests.get(url + params)
# results = json.loads(response.text)['results']
# pprint(results)

# secret = 0
# for event in results:
#     v1 = int(time.time())
#     v2 = int(event['dates'][0]['end'])
#     if 'концерт' in event['title'] and v1 < v2:
#         secret += 1
# pprint(secret)


def clear_description(description):
    res = re.sub('<[^>]*>', '', description)
    return res


# desc = results[0]['description']
# print(desc)
# val1 = clear_description(desc)
# print(val1)


def find_dates(event):
    startdate_dt = datetime.datetime.fromtimestamp(event['dates'][0]['start'])
    enddate_dt = datetime.datetime.fromtimestamp(event['dates'][0]['end'])
    startdate_txt = startdate_dt.strftime('%d-%m-%Y')
    enddate_txt = enddate_dt.strftime('%d-%m-%Y')
    return startdate_dt, enddate_dt, startdate_txt, enddate_txt


# for event in results:
#     startdate_dt, enddate_dt, startdate_txt, enddate_txt = find_dates(event)
#     print(startdate_dt)
#     print(enddate_dt)
#     print(startdate_txt)
#     print(enddate_txt)


def fill_df(src_dic):
    startdate_dt, enddate_dt, startdate_txt, enddate_txt = find_dates(src_dic)
    res_dic = {
        'id': src_dic['id'],
        'title': src_dic['title'],
        'description': clear_description(src_dic['description']),
        'price': src_dic['price'],
        'start_date': startdate_txt,
        'end_date': enddate_txt,
        'url': src_dic['site_url']
    }
    return res_dic


df = pd.DataFrame(columns = 'id title description price start_date end_date url'.split())

# for event in results:
#     # С помощью функции find_dates получаем данные о дате начала и окончания мероприятия в формате datetime
#     # т.к. даты в текстовом формате нам пока не нужны, оставляем на месте соответствующих переменных прочерки
#     start_dt, end_dt, _, _ = find_dates(event)
#     now = datetime.datetime.now()
#     # Проверяем, соответствуют ли даты начала и окончания мероприятия нашим требованиям
#     if (start_dt - now).days < 7 and end_dt > now:
#         # если даты соответствуют, добавляем строку в датафрейм
#         df = df.append(fill_df(event), ignore_index=True)
#
# pprint(df)


def get_data_from_API():
    print('Новый запрос от', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    url = 'https://kudago.com/public-api/v1.4/events/'
    params = '?order_by=-publication_date&location=msk&fields=id,title,dates,description,price,site_url'
    response = requests.get(url+params)
    results = response.json()['results']
    return results


def check_event(event):
    start_dt, end_dt, _, _ = find_dates(event)
    now = datetime.datetime.now()
    if (start_dt-now).days < 7 and end_dt > now:
        return True
    return False


def job():
    global df
    results = get_data_from_API()
    for event in results:
        if check_event(event) and (event['id'] not in list(df['id'])):
            print('Найдено подходящее событие:', event['title'])
            _, _, start_txt, end_txt = find_dates(event)
            print('Событие продлится с {} по {}.'.format(start_txt, end_txt))
            print('Подробности - здесь:', event['site_url'])
            df = df.append(fill_df(event), ignore_index = True)


def make_summary():
    df.to_excel('events.xlsx', index = False)
    print('Новая копия файла events.xlsx создана в', datetime.datetime.now().strftime('%H:%M:%S'))


schedule.every(20).seconds.do(job)
schedule.every().day.at("17:45").do(make_summary)

while True:
    schedule.run_pending()
    time.sleep(1)



