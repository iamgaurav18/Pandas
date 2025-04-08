# cleaning wrong data 

import pandas as pd

df=pd.read_csv('Pandas/data.csv')
print(df.shape)

# replacing the specific value
df['Age'].replace(100, 50, inplace=True) # replace 100 with 50

# replacing the specific value of a specifc row
df.loc[0, 'Age'] = 50 # replace the value of the first row with 50

# replacing the specific value of a specific column
df.loc[0:2, 'Age'] = 50 # replace the value of the first three rows with 50

# replacing values of a large data set based on a condition
for x in df.index: # iterate through the index of the dataframe
    if df.loc[x, 'Age'] > 100: # if the value of the row is greater than 100
        df.loc[x, 'Age'] = 50 # replace the value of the row with 50

# dropping rows based on a condition
for x in df.index: # iterate through the index of the dataframe
    if df.loc[x, 'Age'] > 100: # if the value of the row is greater than 100
        df.drop(x, inplace=True) # drop the row