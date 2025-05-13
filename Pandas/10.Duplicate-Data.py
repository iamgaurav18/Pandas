# working with duplicate data  
#
import pandas as pd
df=pd.read_csv('Pandas/data.csv')
print(df.shape)
# checking for duplicate values
print(df.duplicated()) # check for duplicate values
print(df.duplicated().sum()) # check for duplicate values
# dropping duplicate values
df.drop_duplicates(inplace=True) # drop duplicate values
print(df.shape) # check the shape of the dataframe
# dropping duplicate values based on a specific column
df.drop_duplicates(subset=['Name'], inplace=True) # drop duplicate values based on a specific column
print(df.shape) # check the shape of the dataframe
# dropping duplicate values based on a specific column and keeping the last value
df.drop_duplicates(subset=['Name'], keep='last', inplace=True) # drop duplicate values based on a specific column and keeping the last value
print(df.shape) # check the shape of the dataframe
# how to change the exiting dataframe
df.drop_duplicates(subset=['Name'], keep='last', inplace=True) # drop duplicate values based on a specific column and keeping the last value