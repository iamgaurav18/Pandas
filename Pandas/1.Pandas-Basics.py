# Pandas in python 
# Pandas is a powerful data analysis and manipulation library for Python.
# It provides data structures like Series and DataFrame for handling structured data.
# It is widely used for data analysis, data cleaning, and data visualization.
# It is built on top of NumPy and is designed for working with structured data.

import pandas as pd

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df=pd.DataFrame(data)
print(df)

print(df["Name"][2]) # accessing a column])
# checking pandas version
print(pd.__version__)
