import numpy as np
import pandas as pd
import operator
import json
from pprint import pprint

pd.set_option('display.max_columns', None)
data = pd.read_excel('Fig3-1.xls', header=None, sheet_name='Data')
print(data)

print('-------------------------------------------------------------------------')

df = pd.read_excel("nakladnaya.xls", header=None, skiprows=2, skipfooter=2)
# df = df.dropna()
# print(df)
df = df.dropna(how='all')
print(df)

print('-------------------------------------------------------------------------')

df = pd.read_excel("nakladnaya.xls", header=None, skiprows=2, skipfooter=2)
v1 = data.parse_numbers()[0]
v2 = data.iloc[0, 3].split('от')[0]
v3 = data.iloc[0, 3][2:9]
print(v1)
print(v2)
print(v3)