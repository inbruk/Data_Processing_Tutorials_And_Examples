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

url = 'https://kudago.com/public-api/v1.4/events/'
params = '?order_by=-publication_date&page_size=100&location=msk&fields=id,title,dates,description,price,site_url'
response = requests.get(url + params)
results = json.loads(response.text)['results']
pprint(result)


