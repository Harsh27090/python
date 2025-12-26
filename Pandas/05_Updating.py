import pandas as pd

data= {
    "Name": ["Harsh","Pujan","Krips","Bhavy"],
    "Marks": [74,83,93,84],
    "Grade": ["C","B","A","B"]
}

df= pd.DataFrame(data)

print(df)

# using .loc
# df.loc[row_idx, "Col_Name"] = new_val
df.loc[0, "Marks"] = 81
df.loc[0,"Grade"] = "B"
print(df)
# used to update a specific element

# incrementing "Marks" by 5%
df["Marks"] *= 1.05
print(df)
# used to update an entire column
