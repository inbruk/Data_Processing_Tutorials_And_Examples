import pandas as pd
from IPython.core.display import display

log = pd.read_csv('log.csv')
display(log)

sample = pd.read_csv('sample.csv')
display(sample)

print('-------------------------------------------------------')

columns = sample.columns
display( columns )

print('-------------------------------------------------------')

sample.columns = ['name', 'city', 'age', 'profession']
columns = sample.columns
display( columns )

print('-------------------------------------------------------')

display(log.columns)
log.columns = [ 'user_id', 'time', 'bet', 'win' ]
display(log.columns)

print('-------------------------------------------------------')

users = pd.read_csv('users.csv', delimiter='\t', encoding='koi8_r')
users.columns = [ 'user_id', 'email', 'geo' ]
display(users)

print('-------------------------------------------------------')

sample = pd.read_csv('sample.csv')
display(sample.Name.unique())

print('-------------------------------------------------------')

display(sample.info())

print('-------------------------------------------------------')

display(log.user_id.unique())

print('-------------------------------------------------------')

display(sample)
sample2 = sample[ sample.Age < 30 ]
display(sample2)

print('-------------------------------------------------------')

log = pd.read_csv("log.csv",header=None)
log.columns = ['user_id', 'time', 'bet', 'win']
display(log)

log_win = log[ log.win.notnull() ]
display(log_win)

win_count = len(log_win.index)
display(win_count)

print('-------------------------------------------------------')

display(sample)
sample2 = sample[ (sample.Age < 30) & ( sample.Profession=='Рабочий' ) ]
display(sample2)

print('-------------------------------------------------------')

log = pd.read_csv("log.csv",header=None)
log.columns = ['user_id','time', 'bet','win']
log2 = log.query( 'bet<2000 & win>0' )
display(log2)

print('-------------------------------------------------------')

sample = pd.read_csv("sample.csv")
display(sample)

print('-------------------------------------------------------')

sample3 = sample[ sample.City.str.contains("о", na=False) ]
display(sample3)

print('-------------------------------------------------------')

sample4 = sample[ ~sample.City.str.contains("о", na=False) ]
display(sample4)

print('-------------------------------------------------------')

log = pd.read_csv("log.csv",header=None)
log.columns = ['user_id','time', 'bet','win']
new_log = log[  log.user_id.str.contains("#error", na=False)==False  ]
display(new_log)

print('-------------------------------------------------------')

sample = pd.read_csv("sample.csv")
display(sample)
sample2 = sample.copy(True)
sample2.Age = sample2.Age.apply( lambda x: x+1 )
display(sample2)

print('-------------------------------------------------------')

sample = pd.read_csv("sample.csv")
display(sample)
sample2 = sample.copy(True)
sample2.City = sample2.City.astype(str).apply(lambda x: x.lower())
display(sample2)