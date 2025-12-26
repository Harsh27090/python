import pandas as pd
import numpy as np

data = {
    'Date': pd.date_range('2023-01-01', periods=20),
    'Product': ['A', 'B', 'C', 'D'] * 5,
    'Region': ['East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West',
               'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South'],
    'Sales': np.random.randint(100, 1000, 20),
    'Units': np.random.randint(10, 100, 20),
    'Rep': ['John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary',
            'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice']
}

df = pd.DataFrame(data)
# you can use various aggregation functions
# it is used to view data according to you, what data you want, how you want see it, what should work as index, columns,etc.
print(pd.pivot_table(df,values=['Sales','Units'], index='Region', columns='Product', aggfunc='median'))

# this is based on count
print(pd.crosstab(df['Region'],df['Product']))