import pandas as pd

data= {
    "Name": ["Harsh","Pujan","Krips","Bhavy"],
    "Marks": [74,83,93,84],
    "Grade": ["C","B","A","B"]
}

df= pd.DataFrame(data)

print(df)
# using square bracket : df["Col_Name"] = [val1, val2,....] or ... = df["Col_Name"] * no.
# 1.
df["City"] = ["Surat", "Morbi", "Navsari", "Mahesana"]
print(df)
# 2.
df["Bonus"] = df["Marks"] * 0.1
print(df)

# using insert
# df.insert(loc, "Col_Name", some_data)
df.insert(0, "Stud_ID", [1,2,3,4])
print(df)