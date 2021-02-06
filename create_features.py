import pandas as pd
from IPython.core.display import display

log = pd.read_csv("log.csv", header=None)
sample = pd.read_csv('sample.csv')
users = pd.read_csv('users.csv', delimiter='\t', encoding='koi8_r')

print('-------------------------------------------------------')

log.columns = ['user_id', 'time', 'bet', 'win']
sample.columns = ['name', 'city', 'age', 'profession']
users.columns = ['user_id', 'email', 'geo']

print('-------------------------------------------------------')

display(log['bet'])
log['bet'] = log['bet'].fillna(0)
display(log['bet'])
display(log['bet'].value_counts())
