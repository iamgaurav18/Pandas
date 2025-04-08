# changing data type of columns in a dataframe
# The astype() method is used to change the data type of a column in a DataFrame.

import pandas as pd
df = pd.read_csv('/Users/gauravvishwakarma/Desktop/Code/Pandas/data.csv')
print(df.dtypes) # Displaying the data types of the columns in the DataFrame
# Changing the data type of the Duration column to string
df['Duration'] = df['Duration'].astype(str)
print(df.dtypes) # Displaying the data types of the columns in the DataFrame after changing the data type
print(df.head(10)) # Displaying the first 10 rows of the DataFrame after changing the data type

# Changing the data type of the Duration column to int
df['Duration'] = df['Duration'].astype(int)
print(df.dtypes) # Displaying the data types of the columns in the DataFrame after changing the data type
print(df.head(10)) # Displaying the first 10 rows of the DataFrame after changing the data type

# Changing the data type of the Duration column to float
df['Duration'] = df['Duration'].astype(float)
print(df.dtypes) # Displaying the data types of the columns in the DataFrame after changing the data type
print(df.head(10)) # Displaying the first 10 rows of the DataFrame after changing the data type

