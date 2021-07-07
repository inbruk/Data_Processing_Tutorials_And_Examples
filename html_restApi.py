import numpy as np
import pandas as pd
import operator
import json
from pprint import pprint
import xml.etree.ElementTree as ET
import xmljson
import requests


response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
print(response)


