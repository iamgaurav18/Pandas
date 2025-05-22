# Merge in pandas refers to combining two DataFrames based on one or 
# more common columns (similar to SQL joins). 
# This is done using the pd.merge() function.

import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['B', 'C', 'D'], 'value2': [4, 5, 6]})

# Merge on the 'key' column (inner join by default)
result = pd.merge(df1, df2, on='key')
print(result)

# Merge on the 'key' column (outer join)
result = pd.merge(df1, df2, on='key', how='outer')
print(result)

# Merge on the 'key' column (left join)
result = pd.merge(df1, df2, on='key', how='left')
print(result)

# Merge on the 'key' column (right join)
result = pd.merge(df1, df2, on='key', how='right')
print(result)

# Merge on multiple keys
df3 = pd.DataFrame({'key1': ['A', 'B', 'C'], 'key2': [1, 2, 3], 'value1': [7, 8, 9]})
df4 = pd.DataFrame({'key1': ['B', 'C', 'D'], 'key2': [2, 3, 4], 'value2': [10, 11, 12]})
# Merge on multiple keys
result = pd.merge(df3, df4, on=['key1', 'key2'])
print(result)