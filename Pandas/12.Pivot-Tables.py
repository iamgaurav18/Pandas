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