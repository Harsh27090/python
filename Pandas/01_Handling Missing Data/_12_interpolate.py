import pandas as pd

data= {
    "ID": [1, None, 3, 4],
    "Name": ["Harsh","Pujan" ,"Krips","Bhavy"],
    "Age": [20,None,19,20],
    "Marks": [74,None,93,84],
    "Grade": ["C","B","A","B"],
    "City": ["Surat", "Morbi", "Navsari", "Mehsana"]
}

df= pd.DataFrame(data)
print(df)

df["ID"] = df["ID"].interpolate(method="linear")
print(df)

# df.interpolate(method="linear", axis=0, inplace=True)
# print(df)