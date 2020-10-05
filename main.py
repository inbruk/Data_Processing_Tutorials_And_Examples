import pandas as pd

lst = list(range(10, 1001))
data = pd.Series(lst)
print(data.loc[10] + data.loc[23] - data.loc[245] + data.iloc[122])