import pandas as pd
from IPython.core.display import display

ratings_df = pd.read_csv('ratings.csv')
movies_df = pd.read_csv('movies.csv')

print('-------------------------------------------------------')

print(ratings_df.head())
print(movies_df.head())
print(movies_df.columns)

print('-------------------------------------------------------')

genres_vc = movies_df['genres'].value_counts()
display(genres_vc)

print('-------------------------------------------------------')

display(movies_df.columns.tolist())

print('-------------------------------------------------------')

display(ratings_df['rating'].min())
display(ratings_df['rating'].max())

print('-------------------------------------------------------')

movies_len = len(movies_df)
display(movies_len)

print('-------------------------------------------------------')

joined = ratings_df.merge(movies_df, on='movieId', how='left')
display(joined.head())
display(movies_df.columns)

print('-------------------------------------------------------')


