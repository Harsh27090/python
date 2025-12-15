"""
1. how big is the data: no. of rows and columns
2. names of columns

shape and columns
"""

import pandas as pd

data= {
    "Name": ["Harsh","Pujan","Krips","Bhavy"],
    "Marks": [74,83,93,84],
    "Grade": ["C","B","A","B"]
}

df= pd.DataFrame(data)

print(df)
print(f"Shape: {df.shape}")
print({f"Columns: {df.columns}"})
