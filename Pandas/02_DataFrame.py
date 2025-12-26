import pandas as pd
import numpy as np

data = {
    'Name': ['Harsh', 'Pujan', 'Krips', 'Bhavy', 'Divy'],
    'Marks': [46,65,999,67,75]
}

df = pd.DataFrame(data)
print(df)

data_list = [
    ['Harsh', 46],
    ['Pujan', 65],
    ['Krips', 999],
    ['Bhavy', 75],
    ['Divy', 67]
]
# no column names
df2 = pd.DataFrame(data_list)
print(df2)
col_names = ['Name', 'Marks']
df3 = pd.DataFrame(data_list, columns=col_names)
print(df3)