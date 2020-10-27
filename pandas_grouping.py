import pandas as pd
from IPython.core.display import display

football = pd.read_csv('data_sf.csv')
df = football

print('-------------------------------------------------------')

small_df = df[df.columns[1:8]].head(25)
display(small_df)

print('-------------------------------------------------------')