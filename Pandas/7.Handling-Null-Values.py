# Handling Null or empty values in Pandas DataFrame

import pandas as pd

df=pd.read_csv('/Users/gauravvishwakarma/Desktop/Code/Pandas/data.csv')

# check if there any null or empty values in the DataFrame
print(df.isnull().sum()) # Displaying the number of null values in each column
print(df.isna().sum()) # Displaying the number of null values in each column
print(df.notnull().sum()) # Displaying the number of non-null values in each column

# to deal with empty values we have two ways
# 1. Drop the rows or columns with null values
new_df = df.dropna() # Drop the rows with null values
# new_df = df.dropna(axis=1) # Drop the columns with null values
# new_df = df.dropna(axis=0) # Drop the rows with null values
new_df = df.dropna(subset=['Duration']) # Drop the rows with null values in the Duration column
# or
#df.dropna(axis=1, inplace=True) # Drop the columns with null values
# axis=0 means rows and axis=1 means columns
# inplace=True means that the changes will be made to the original DataFrame
print(new_df)

# 2. Fill the null values with a specific value
df.fillna(0, inplace=True) # Fill the null values with 0

# replace only for specific column
df['Duration'].fillna(0, inplace=True) # Fill the null values in the Duration column with 0

# replace empty values with mean 
df['Duration'].fillna(df['Duration'].mean(), inplace=True) # Fill the null values in the Duration column with mean

# replace empty values with median
df['Duration'].fillna(df['Duration'].median(), inplace=True) # Fill the null values in the Duration column with median

# replace empty values with mode
df['Duration'].fillna(df['Duration'].mode()[0], inplace=True) # Fill the null values in the Duration column with mode
# mode()[][0] means that we are taking the first value of the mode
# mode() returns a Series object and we are taking the first value of the Series object
# mode() returns the most frequent value in the column

# replace empty values with forward fill
df.fillna(method='ffill', inplace=True) # Fill the null values with forward fill
# forward fill means that the null values will be filled with the previous value

# replace empty values with backward fill
df.fillna(method='bfill', inplace=True) # Fill the null values with backward fill