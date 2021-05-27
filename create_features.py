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

print('-------------------------------------------------------')

log = pd.read_csv("log.csv", header=None)
log.columns = ['user_id', 'time', 'bet', 'win']
display(log)

# log = log.dropna(subset=['time'])
# display(log)


# def fillna_win(row):
#
#     if nu.isnan(row.win):
#         if nu.isnan(row.bet):
#             return 0
#         else:
#             return -row.bet
#     else:
#         return row.win
#
#
# log['win'] = log.apply(lambda row: fillna_win(row), axis=1)
# display(log)


def fillna_win(row):
    if nu.isnan(row.win):
        return 0
    else:
        return row.win


def fillna_bet(row):
    if nu.isnan(row.bet):
        return 0
    else:
        return row.bet


def fill_net(row):
    return row.win - row.bet


log['win'] = log.apply(lambda row: fillna_win(row), axis=1)
log['bet'] = log.apply(lambda row: fillna_bet(row), axis=1)
log['net'] = log.apply(lambda row: fill_net(row), axis=1)

betser = log.bet[log.bet > 0]
netser = log.net[log.bet > 0]
display(betser.count())
display(log.bet.count())

display(485/1000)

display(betser.mean())
display(netser.mean())

netser = log.net[log.net < 0]
display(netser.mean())
display(netser.count())

netser = log.net[log.net > 0]
display(netser.count())

print('-------------------------------------------------------')

log = pd.read_csv("log.csv", header=None)
log.columns = ['user_id', 'time', 'bet', 'win']
min_st = log['bet'].dropna().min()
min_bet_amount = log.bet[log.bet == min_st].count()
display(min_bet_amount)

print('-------------------------------------------------------')

log = pd.read_csv("log.csv", header=None)
users = pd.read_csv('users.csv', delimiter='\t', encoding='koi8_r')

log.columns = ['user_id', 'time', 'bet', 'win']
users.columns = ['user_id', 'email', 'geo']

def fillna_win(row):
    if nu.isnan(row.win):
        return 0
    else:
        return row.win


def fillna_bet(row):
    if nu.isnan(row.bet):
        return 0
    else:
        return row.bet


def fill_net(row):
    return row.win - row.bet


log['win'] = log.apply(lambda row: fillna_win(row), axis=1)
log['bet'] = log.apply(lambda row: fillna_bet(row), axis=1)
log['net'] = log.apply(lambda row: fill_net(row), axis=1)


def prepare_user_id(s):
    arr_str = s.split(' - ')
    if len(arr_str)>1:
        res_str = arr_str[1]
        list_str = list(res_str)
        list_str[0] = 'U'
        res_str = "".join(list_str)
        return res_str
    else:
        return ''


log['user_id'] = log.user_id.apply( prepare_user_id )

display(log)
display(users)

res_df = pd.merge(log, users, on='user_id')
display(res_df)

print('-------------------------------------------------------')

res = res_df.groupby('user_id').net.sum().median()
display(res)

print('B6.5.2.2 -------------------------------------------------------')

users_with_bets = res_df[res_df.bet > 0].user_id.drop_duplicates()
ures_df = pd.merge(log, users_with_bets, on='user_id')
display(ures_df)
ures_grouped = ures_df[res_df.bet == 0.0].groupby('user_id').bet.count()
display(ures_grouped.median())

print('B6.5.2.3 -------------------------------------------------------')


def prepare_time(st):
    res_f = st.replace('[', '')
    return res_f


res_df.time = res_df.time.dropna()
res_df.time = res_df.time.apply(prepare_time)
res_df['time'] = pd.to_datetime(res_df['time'], format='%Y-%m-%d %H:%M:%S')
# display(res_df)

res_bet0_min = res_df[res_df.bet == 0.0].groupby('user_id').time.min()
res_betp_min = res_df[res_df.bet > 0.0].groupby('user_id').time.min()
res_bet_df = pd.merge(res_bet0_min, res_betp_min, on='user_id')
# display(res_bet_df)

res_bet_df['time_d'] = res_bet_df['time_y'] - res_bet_df['time_x']
# display(res_bet_df)

display(res_bet_df.time_d.mean())

print('B6.5.3.1 ------------------------------------------------')
res = res_df.groupby('geo').win.sum().sort_values()
display(res)

print('B6.5.3.2 ------------------------------------------------')
res = res_df[res_df.bet > 0.0]
display(res)

res = res.groupby('geo').bet.mean()
display(res)

max_mean_bet = res.max()
display(max_mean_bet)

min_mean_bet = res.min()
display(min_mean_bet)

display(max_mean_bet/min_mean_bet)

print('B6.5.3.3 ------------------------------------------------')

log = pd.read_csv("log.csv", header=None)
users = pd.read_csv('users.csv', delimiter='\t', encoding='koi8_r')

log.columns = ['user_id', 'time', 'bet', 'win']
users.columns = ['user_id', 'email', 'geo']

log.user_id.dropna()

def prepare_user_id(s):
    arr_str = s.split(' - ')
    if len(arr_str)>1:
        res_str = arr_str[1]
        list_str = list(res_str)
        list_str[0] = 'U'
        res_str = "".join(list_str)
        return res_str
    else:
        return ''


log['user_id'] = log.user_id.apply( prepare_user_id )
res_df = pd.merge(log, users, on='user_id')
#sample2 = res_df[res_df.bet > 0.0].groupby(['geo']).bet.count()
sample2 = res_df.groupby('geo').user_id.count()

display(sample2)





