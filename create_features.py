import numpy as nu
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

print('-------------------------------------------------------')

log = pd.read_csv("log.csv", header=None)
log.columns = ['user_id', 'time', 'bet', 'win']
display(log)


def fillna_win(row):

    if nu.isnan(row.win):
        if nu.isnan(row.bet):
            return 0
        else:
            return -row.bet
    else:
        return row.win


log['win'] = log.apply(lambda row: fillna_win(row), axis=1)
display(log)

#res = log['win'].value_counts()
#display(res)

print('-------------------------------------------------------')

def fill_net(row):
    if row.win < 0:
        return 0
    else:
        return row.win - row.bet


log['net'] = log.apply(lambda row: fill_net(row), axis=1)
display(log)


def get_positive(x):
    if x > 0: return x

res = log['net'].apply(lambda x: get_positive(x) ).dropna().median()
display(res)

print('-------------------------------------------------------')

log = pd.read_csv("log.csv", header=None)
log.columns = ['user_id', 'time', 'bet', 'win']
#res = log['bet'].dropna().mean()
#res = log.bet.mean()
#res = log.bet.sum() / log.bet.dropna().shape[0]
res = nu.mean(log.bet)
display(res)
