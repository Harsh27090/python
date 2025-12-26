import pandas as pd

data= {
    "Name": ["Harsh",None ,"Krips","Bhavy"],
    "Age": [20,None,19,20],
    "Marks": [74,None,93,84],
    "Grade": ["C",None,"A","B"],
    "City": ["Surat", None, "Navsari", "Mehsana"]
}

df= pd.DataFrame(data)
print(df)
print(df.isna())
print(df.isna().sum())
print(df.isnull()) # isna = isnull, you can use whichever you want
print(df.isnull().sum())
print(df.isna().any())

