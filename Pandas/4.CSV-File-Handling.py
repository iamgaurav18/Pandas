# Working with CSV files using pandas module only
# Importing the pandas library

import pandas as pd

# Reading a CSV file
df = pd.read_csv('/Users/gauravvishwakarma/Desktop/Code/Pandas/data.csv')

# Displaying the first 5 rows of the DataFrame
print(df.head())

# Displaying the last 5 rows of the DataFrame
print(df.tail())

# Displaying the number of rows and columns in the DataFrame    
print(df.shape)

# Displaying the column names of the DataFrame
print(df.columns)

# Displaying the data types of the columns
print(df.dtypes)

# Displaying the summary statistics of the DataFrame
print(df.describe())

# Selecting a column
print(df['Duration'])

# Selecting multiple columns
print(df[['Duration', 'Pulse']])

# Selecting rows using index
print(df.loc[1])

# Selecting rows using condition
print(df[df['Pulse'] > 30])

print(f"Printing entire Datafrane of size: {df.shape}")
# Displaying the entire DataFrame
# Note: This will print the entire DataFrame, which may be large
print(df)

# creating a new CSV file
df.to_csv('/Users/gauravvishwakarma/Desktop/Code/Pandas/new_data.csv', index=False)

#writing data to an existing CSV file
df.to_csv('/Users/gauravvishwakarma/Desktop/Code/Pandas/data.csv', mode='a', header=False, index=False)

# Note: The to_csv() method is used to write the DataFrame to a CSV file

# mode 'a' is used to append data to the existing file
# mode 'w' is used to write data to a new file
# mode 'r' is used to read data from the existing file
# mode 'r+' is used to read and write data to the existing file
# mode 'a+' is used to read and append data to the existing file
# Note: The index=False parameter is used to avoid writing the index column to the CSV file
# Note: The header=False parameter is used to avoid writing the header row to the CSV file
# Note: The mode parameter is used to specify the mode in which the file should be opened

# differences between loc and iloc
# loc is label based indexing
# iloc is position based indexing
# loc is used to access a group of rows and columns by labels or a boolean array
# iloc is used to access a group of rows and columns by integer position(s)
# loc is inclusive of the last element
# iloc is exclusive of the last element