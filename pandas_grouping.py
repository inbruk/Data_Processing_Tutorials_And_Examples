import pandas as pd
from IPython.core.display import display

football = pd.read_csv('data_sf.csv')
df = football

print('-------------------------------------------------------')

small_df = df[df.columns[1:8]].head(25)
display(small_df)

print('-------------------------------------------------------')

s = small_df['Nationality'].value_counts()
display(s)

print('-------------------------------------------------------')

fk = df['Club'].value_counts()
print(len(fk))

print('-------------------------------------------------------')

a = df['Age'].value_counts(normalize=True)
display(a)

print('-------------------------------------------------------')

w = df['Wage'].value_counts(bins=4)
display(w)

print('-------------------------------------------------------')

ws = small_df['Wage'].value_counts(bins=4)
display(small_df.loc[(small_df['Wage'] > ws.index[3].left) & (small_df['Wage'] <= ws.index[3].right)])

print('-------------------------------------------------------')

ak = df['FKAccuracy'].value_counts(bins=5)
display(ak)
display(ak.index[4].left)
display(ak.index[4].right)

print('-------------------------------------------------------')

display(df['Position'].nunique())

print('-------------------------------------------------------')

sn = small_df['Nationality'].value_counts()
sn_df = sn.reset_index()
sn_df.columns = ['Nationality', 'Players Count']
display(sn_df)

print('-------------------------------------------------------')

spa = df[df.Nationality == 'Spain']
display(len(spa))
spa_wage_vc = spa['Wage'].value_counts(bins=4)
display(spa_wage_vc)

display(round(651.0 / 671.0, 2))

print('-------------------------------------------------------')

age = df[df.Age > 35]
age_club = age[(age.Club == 'Nagoya Grampus') | (age.Club == 'Club Atlético Huracán') | (age.Club == 'LA Galaxy')]
age_club_vk = age_club['Club'].value_counts()
display(age_club_vk)

print('-------------------------------------------------------')

club = df[(df.Nationality == 'Argentina')]
club_age = club['Age'].value_counts(bins=4)
display(club_age)

print('-------------------------------------------------------')

spain = df[df.Nationality == 'Spain']
spain_age = spain[spain.Age == 21]
display(round(len(spain_age)*100/len(spain),2))

print('-------------------------------------------------------')

grouped_df = df.groupby(['Position'])['Wage'].sum().reset_index()
filtered_df = grouped_df[ grouped_df.Wage > 5000000 ]
display( filtered_df )




