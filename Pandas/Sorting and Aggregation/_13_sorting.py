# df.sort_values(by="Col_Name", ascending=True/False, inplace=True/False)
# df.sort_values(by=["Col1_Name", "Col2_Name"], ascending=[True/False, True/False], inplace=True/False)

import pandas as pd

data= {
    "ID": [1, 2, 3, 4],
    "Name": ["Harsh","Pujan" ,"Krips","Bhavy"],
    "Age": [20,18,19,20],
    "Marks": [74,85,93,84],
    "Grade": ["C","B","A","B"],
    "City": ["Surat", "Morbi", "Navsari", "Mehsana"]
}

df= pd.DataFrame(data)
print(df)

df.sort_values(by="Age", ascending=False, inplace=True)
print(df)

df.sort_values(by=["Age", "Marks"], ascending=[True,False], inplace=True)
print(df)