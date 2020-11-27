import matplotlib.pyplot as plt
import  pandas as pd
from IPython.core.display import display

print('-------------------------------------------------------')

df = pd.read_csv('tips.csv')
display(df)

print('-------------------------------------------------------')

df.plot()
plt.show()

print('-------------------------------------------------------')