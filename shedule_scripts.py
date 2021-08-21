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

url = 'https://kudago.com/public-api/v1.4/events/'
params = '?order_by=-publication_date&page_size=100&location=msk&fields=id,title,dates,description,price,site_url'
response = requests.get(url + params)
results = json.loads(response.text)['results']
pprint(results)

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

