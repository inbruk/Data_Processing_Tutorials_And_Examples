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
          'dimensions': 'ym:s:date,ym:s:deviceCategory,ym:s:mobilePhone,ym:s:mobilePhoneModel',
          'date1': '2019-05-01',
          'date2': '2019-05-31',
          'ids': 30177909,
          'offset': 1,
          'limit': 500
          }

response = requests.get('https://api-metrika.yandex.net/stat/v1/data', params=params, headers=headers)
# print(response.status_code)

metrika_data = response.json()
pprint(metrika_data)

print('------------------------------------------------------------------------------------')

data = metrika_data['data']
data_lst = list(map(lambda x:
                    {
                        'date': x['dimensions'][0]['name'],
                        'deviceCategory': x['dimensions'][1]['name'],
                        'mobilePhone': x['dimensions'][2]['name'],
                        'mobilePhoneModel': x['dimensions'][3]['name'],
                        'usersCount': x['metrics'][0]
                    },
                    data))
# pprint(data_lst)
resp_df = pd.DataFrame(data_lst)
pprint(resp_df)

# print('------------------------------------------------------------------------------------')
#
# rev_sum = revenue_data['revenue'].sum()
# pprint(round(rev_sum))

print('------------------------------------------------------------------------------------')

resp_df = resp_df.fillna('None')
pprint(resp_df)

print('------------------------------------------------------------------------------------')

resp_df = resp_df.groupby(['deviceCategory', 'mobilePhone', 'mobilePhoneModel']).sum()
pprint(resp_df.count())
resp_df = resp_df[resp_df.usersCount >= 3.0]
pprint(resp_df.count())

print('------------------------------------------------------------------------------------')

res_df = pd.merge(revenue_data, resp_df, on=['deviceCategory', 'mobilePhone', 'mobilePhoneModel'])
pprint(res_df)

print('------------------------------------------------------------------------------------')

res_df['ARPU'] = round(res_df.revenue / res_df.usersCount, 2)
res_df = res_df[res_df.usersCount >= 3.0]
res_df = res_df.sort_values(by=['ARPU'], ascending=False)
pprint(res_df)

