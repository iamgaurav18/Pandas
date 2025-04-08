# JSON File Handling
# JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate.
# It is often used for transmitting data in web applications between a server and a client.
# JSON files are similar to CSV files but are more flexible and can represent complex data structures.
# JSON files can be read and written using the pandas library in Python.

# Importing the pandas library
import pandas as pd

# Reading a JSON file
df=pd.read_json('/Users/gauravvishwakarma/Desktop/Code/Pandas/data.json')
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

print(df.to_string()) # Displaying the entire DataFrame
# Note: This will print the entire DataFrame, which may be large

# Writing a DataFrame to a JSON file
df.to_json('/Users/gauravvishwakarma/Desktop/Code/Pandas/data1.json', orient='records', lines=True)
# The 'orient' parameter specifies the format of the JSON file.
# The 'lines' parameter specifies whether to write each record on a separate line.