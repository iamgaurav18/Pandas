import pandas as pd

data = {
    'City': ['NY', 'NY', 'LA', 'LA'],
    'Year': [2020, 2021, 2020, 2021],
    'Sales': [250, 300, 200, 250]
}
df = pd.DataFrame(data)

# Create a pivot table
pivot = df.pivot_table(values='Sales', index='City', columns='Year', aggfunc='sum')
# pivot table() will create a new dataframe with the unique values of the index and columns
print(pivot)

# A pivot table in pandas is a powerful tool that allows you to summarize, aggregate, 
# and reorganize data in a DataFrame. It helps you transform long data into a summarized 
# table by grouping data based on one or more keys and applying aggregation functions 
# (like sum, mean, count, etc.).

# it is similar to the groupby() method, but it allows you to create a new dataframe
# with the unique values of the index and columns
# The pivot_table() function takes the following parameters:
# - data: The DataFrame to be used for creating the pivot table.
# - values: The column(s) to be aggregated.
# - index: The column(s) to be used as the index (rows) of the pivot table.
# - columns: The column(s) to be used as the columns of the pivot table.
# - aggfunc: The aggregation function to be applied (default is 'mean').
# - fill_value: Value to replace missing values in the pivot table (default is None).
# - margins: If True, adds all row/column totals (default is False).
# - margins_name: Name of the row/column that contains the totals (default is 'All').
# - dropna: If True, do not include columns whose entries are all NaN (default is True).