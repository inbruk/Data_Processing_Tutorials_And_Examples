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


token = 'AQAAAABXjzIIAAdSVYTRaTUWbUtzlhqF3lZc5uM'
headers = {'Authorization': 'OAuth ' + token}
params = {'metrics': 'ym:s:visits,ym:s:pageviews',
          'dimensions': 'ym:s:referer',
          'date1': '2019-06-01',
          'date2': '2019-06-10',
          'ids': 30177909}

response = requests.get('https://api-metrika.yandex.net/stat/v1/data', params=params, headers=headers)
# print(response.status_code)

metrika_data = response.json()
# pprint(metrika_data)

print(metrika_data.keys())
print(metrika_data['total_rows'])
pprint(metrika_data['query'])
pprint(metrika_data['data'])

print('-------------------------------------------------------------------------------------------------------')

# Создаём пустой список, в который будем добавлять словари в новом формате
result = []
# Начинаем перебор элементов старого отчёта (только раздел с данными)
for data_item in metrika_data['data']:
    # Создаём словарь для хранения текущих данных в новом формате
    new_dict = {}
    # Обращаемся к разделу отчёта, содержащего метаданные
    # Перебираем названия группировок, которые использовались в отчёте
    for i, dimension in enumerate(data_item['dimensions']):
        # Создаём в новом словаре ключ для каждой группировки
        # Устанавливаем значение для каждого ключа
        new_dict[metrika_data['query']['dimensions'][i]] = dimension['name']
    # Те же действия выполняем для метрик
    for i, metric in enumerate(data_item['metrics']):
        new_dict[metrika_data['query']['metrics'][i]] = metric
    # Добавляем созданный словарь в итоговый список result
    result.append(new_dict)
pprint(result)

print('-------------------------------------------------------------------------------------------------------')












