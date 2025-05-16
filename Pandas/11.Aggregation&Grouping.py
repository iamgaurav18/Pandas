# creating a dataframe from a list
# df = pd.DataFrame([['Gaurav', 25], ['Vishwakarma', 30]], columns=['Name', 'Age'])

import pandas as pd

# creating a dataframe with only integer values from a list
df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['A','B','C'])

# displaying the dataframe
print(df)

# sum of all the values in the dataframe in each column
print(df.sum())

# instead of sum, we can use mean, median, min, max, std, var, count all at once using describe
print(df.describe())

# agg() method is used to apply multiple aggregation functions to the dataframe
print(df.agg(['sum','mean','min','max','std','var','count']))
# Note: The agg() method is used to apply multiple aggregation functions to the dataframe

# how to access each value of these results for example i want to access the mean of column A
print(df.agg(['sum','mean','min','max','std','var','count'])['A']['mean'])

# grouping the dataframe by column A and applying the sum function
print(df.groupby('A')['C'].sum())
# Note: The groupby() method is used to group the dataframe by one or more columns

# grouping the dataframe by column A and B and applying the sum function
print(df.groupby(['A','B'])['C'].sum())
