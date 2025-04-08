# head method in pandas
# The head() method is used to return the first n rows of a DataFrame.

import pandas as pd
df=pd.read_csv('/Users/gauravvishwakarma/Desktop/Code/Pandas/data.csv')
print(df.head(10)) # Displaying the first 10 rows of the DataFrame

# tail method in pandas
# The tail() method is used to return the last n rows of a DataFrame.
print(df.tail(10)) # Displaying the last 10 rows of the DataFrame

print(df.info) # Displaying the information about the DataFrame

print(df.columns) # Displaying the column names of the DataFrame

print(df[df['Duration']> 60]) # Displaying the rows where the Duration is greater than 60
print(df[df['Duration']> 60].head(10)) # Displaying the first 10 rows where the Duration is greater than 60

print(df.loc[0:5]) # Displaying the first 5 rows of the DataFrame using loc
print(df.iloc[0:5]) # Displaying the first 5 rows of the DataFrame using iloc
print(df.iloc[0:5, 0:2]) # Displaying the first 5 rows and first 2 columns of the DataFrame using iloc
print(df.iloc[0:5, [0, 2]]) # Displaying the first 5 rows and first and third columns of the DataFrame using iloc

# renaming columns
df.rename(columns={'Duration': 'Time'}, inplace=True) # Renaming the Duration column to Time
print(df.head(10)) # Displaying the first 10 rows of the DataFrame after renaming the column