# apply in pandas is used to apply a function along an axis (rows or columns) of a DataFrame or to a Series. 
# It is useful for performing custom operations on your data.

import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Apply a function to each column (default axis=0)
result = df.apply(lambda x: x.max() - x.min()) # x.max() - x.min() will return the difference between the max and min value of each column
print(result)

# Apply a function to each row (axis=1)
result = df.apply(lambda x: x.sum(), axis=1) # x.sum() will return the sum of each row
print(result)

# Apply a function to a specific column
result = df['A'].apply(lambda x: x ** 2) # x ** 2 will return the square of each value in column A
print(result)

# Apply a function to a specific row
result = df.iloc[0].apply(lambda x: x + 1) # x + 1 will return the value of each column in the first row plus 1
print(result)

# we can also use any regular expression or method in apply

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Define a regular function
def add_ten(x):
    return x + 10

# Apply the function to column 'A'
result = df['A'].apply(add_ten)
print(result)