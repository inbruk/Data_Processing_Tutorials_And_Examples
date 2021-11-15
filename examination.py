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
