# Concatenation in Pandas
# Concatenation in pandas refers to combining two or more DataFrames or 
# Series along a particular axis (rows or columns). 
# This is commonly done using the pd.concat() function.

import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

# Concatenate along rows (default, axis=0)
result = pd.concat([df1, df2])
print(result)

# Concatenate along columns (axis=1)
result = pd.concat([df1, df2], axis=1)
print(result)

# Concatenate with keys
result = pd.concat([df1, df2], keys=['df1', 'df2'])
print(result)

# Concatenate with ignore_index
result = pd.concat([df1, df2], ignore_index=True)
print(result)

# Concatenate with join
result = pd.concat([df1, df2], join='outer')  # outer join (default)
print(result)
result = pd.concat([df1, df2], join='inner')  # inner join
print(result)

# Concatenate with axis=1 and join='inner'
result = pd.concat([df1, df2], axis=1, join='inner')
print(result)