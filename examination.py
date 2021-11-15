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

revenue_data = pd.read_csv("revenue_data.csv", sep='\t', decimal=',')
pprint(revenue_data)
pprint('------------------------------------------------------------------------------------')


token = 'AQAAAABXjzIIAAdSVYTRaTUWbUtzlhqF3lZc5uM'
headers = {'Authorization': 'OAuth ' + token}
params = {'metrics': 'ym:s:users',
          'dimensions': 'ym:s:deviceCategory,ym:s:mobilePhone,ym:s:mobilePhoneModel',
          'date1': '2019-05-01',
          'date2': '2019-05-31',
          'ids': 30177909}

response = requests.get('https://api-metrika.yandex.net/stat/v1/data', params=params, headers=headers)
# print(response.status_code)

metrika_data = response.json()
pprint(metrika_data)
print('------------------------------------------------------------------------------------')


df = pd.DataFrame(columns=['deviceCategory', 'mobilePhone', 'mobilePhoneModel', 'usersCount'])
#pprint(df)

# lst = metrika_data['data']
# pprint(lst)

curr_item = metrika_data['data'][0]
pprint(curr_item)
print('------------------------------------------------------------------------------------')

curr_dims = curr_item['dimensions']
curr_deviceCategory = curr_dims[0]['name']
curr_mobilePhone = curr_dims[1]['name']
curr_mobilePhoneModel = curr_dims[2]['name']
pprint(str(curr_deviceCategory) + ' ' + str(curr_mobilePhone) + ' ' + str(curr_mobilePhoneModel))
print('------------------------------------------------------------------------------------')

curr_met = curr_item['metrics']
curr_usr_count = curr_met[0]
pprint(str(curr_usr_count))
print('------------------------------------------------------------------------------------')

# res_lst = list(filter(lambda x: 'Python' in x['dimensions'][0]['name'], metrika_data))
# pprint(res_lst)


