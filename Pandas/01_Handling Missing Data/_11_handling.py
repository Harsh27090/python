import pandas as pd

data= {
    "ID": [1, None, 3, 4],
    "Name": ["Harsh",None ,"Krips","Bhavy"],
    "Age": [20,None,19,20],
    "Marks": [74,None,93,84],
    "Grade": ["C",None,"A","B"],
    "City": ["Surat", None, "Navsari", "Mehsana"]
}

df= pd.DataFrame(data)
print(df)
# 1. .dropna(): the missing value is removed from the df
# .dropna(axis=0/1, inplace=True/False), 0->row, 1->column
# df.dropna(axis=0, inplace=True)
# print(df)
# df.dropna(thresh=2, inplace=True) # it means cols with more than 2 missing values will be removed

#2. .fillna(): the missing value is replaced by the provided value
# .fillna(value, inplace=True/False)
# df.fillna(value=0, inplace=True)
# print(df)

# replace the missing value using the data of the column
# df["Marks"].fillna(df["Marks"].mean(), inplace=True)
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)