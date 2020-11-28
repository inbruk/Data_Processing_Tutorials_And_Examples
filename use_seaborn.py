import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings; warnings.simplefilter('ignore')

df = pd.read_csv('tips.csv')
sns.set()
sns.distplot(df['total_bill'])
plt.show()

print('-------------------------------------------------------')

sns.jointplot(x = 'total_bill', y = 'tip', data = df, kind = 'reg')
plt.show()

print('-------------------------------------------------------')

sns.pairplot(df)
plt.show()

print('-------------------------------------------------------')





