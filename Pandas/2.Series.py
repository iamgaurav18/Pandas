# Series in Pandas
# A Series is a one-dimensional labeled array capable of holding data 
# of any type (integer, string, float, python objects, etc.).
# The axis labels are collectively called the index.
# A Series can be created using a list, dictionary, or NumPy array.
# Importing the pandas library
import pandas as pd
# Creating a Series from a list
data = [1, 2, 3, 4, 5]
s = pd.Series(data)     
print(s)
# Creating a Series from a dictionary
data = {'a': 1, 'b': 2, 'c': 3} # here a,b,c are the indeces of the series
s = pd.Series(data)
print(s)

# creating labels
data = [1, 2, 3, 4, 5]
labels = ['A', 'B', 'C', 'D', 'E']
s = pd.Series(data, index=labels)
print(s)
print(s['A']) # accessing values using labels
print(s[0]) # accessing values using index
print(s.iloc[0]) # accessing values using index
print(s.loc['A']) # accessing values using labels
print(s['A':'C']) # accessing values using labels