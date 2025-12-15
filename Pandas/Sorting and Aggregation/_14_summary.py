"""
df["col_name"].mean()
df["col_name"].min()
df["col_name"].max()
df["col_name"].sum()
.std()
...
"""

import pandas as pd
data={
    "Name": ["Harsh", "Pujan", "Shyam", "Krips"],
    "Marks": [84,93,87,96],
    "City": ["Surat", "Morbi", "Surat", "Navsari"]
}

df=pd.DataFrame(data)
avg_marks=df["Marks"].mean()
print(avg_marks)
