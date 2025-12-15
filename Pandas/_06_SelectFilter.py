import pandas as pd

data= {
    "Name": ["Harsh","Pujan","Krips","Bhavy"],
    "Marks": [74,83,93,84],
    "Grade": ["C","B","A","B"]
}

df= pd.DataFrame(data)

print(df)

print("\nSingle column (returns a series):")
print(df["Name"])
print("\nMultiple columns (returns a dataframe) :")
print(df[["Name", "Marks"]])

print(df[df["Marks"]>80])
print(df[(df["Marks"]>80) & (df["Marks"]<90)])