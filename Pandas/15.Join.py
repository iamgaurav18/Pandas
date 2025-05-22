# Join in pandas refers to combining two DataFrames based on their 
# indexes or a key column, similar to SQL joins. 
# This is typically done using the .join() method or the pd.merge() function.

import pandas as pd

# Create two DataFrames with the same index
df1 = pd.DataFrame({'A': [1, 2, 3]}, index=['x', 'y', 'z'])
df2 = pd.DataFrame({'B': [4, 5, 6]}, index=['x', 'y', 'z'])

# Join df2 to df1 based on the index
result = df1.join(df2)
print(result)

# Join with different index
df3 = pd.DataFrame({'B': [7, 8]}, index=['x', 'y'])
df4 = pd.DataFrame({'C': [9, 10]}, index=['y', 'z'])
# Join df3 to df4 based on the index
result = df3.join(df4, how='outer')
print(result)

# Join with different index and columns
df5 = pd.DataFrame({'A': [11, 12]}, index=['a', 'b'])
df6 = pd.DataFrame({'B': [13, 14]}, index=['b', 'c'])
# Join df5 to df6 based on the index
result = df5.join(df6, how='inner')
print(result)

# Join with columns only 
df7 = pd.DataFrame({'A': [15, 16]}, index=['a', 'b'])
df8 = pd.DataFrame({'B': [17, 18]}, index=['b', 'c'])
# Join df7 to df8 based on the columns
result = df7.join(df8, how='outer')
print(result)

# Join with columns only and different index
df9 = pd.DataFrame({'A': [19, 20]}, index=['a', 'b'])
df10 = pd.DataFrame({'B': [21, 22]}, index=['b', 'c'])
# Join df9 to df10 based on the columns
result = df9.join(df10, how='inner')
print(result)