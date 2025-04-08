# DataFrame in Pandas
# DataFrame is a 2-dimensional labeled data structure with columns 
# of potentially different types.
# It is similar to a spreadsheet or SQL table, 
# or a dictionary of Series objects.
# DataFrame is generally the most commonly used pandas object.

import pandas as pd

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df=pd.DataFrame(data)
print(df)
print(df['Name']) # Accessing a column

print(df[['Name', 'City']]) # Accessing multiple columns

# Accessing rows using index
print(df.loc[1]) # Accessing the second row

# Accessing rows using condition
print(df[df['Age'] > 30]) # Accessing rows where age is greater than 30

# Adding a new column
df['Salary'] = [50000, 60000, 70000]
print(df)

# iloc is used for integer-location based indexing
print(df.iloc[0]) # Accessing the first row
print(df.iloc[:, 1]) # Accessing the second column

# naming the index
df.index = ['a', 'b', 'c']
print(df)
