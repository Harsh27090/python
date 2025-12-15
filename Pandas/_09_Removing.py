import pandas as pd

data= {
    "Name": ["Harsh","Pujan","Krips","Bhavy"],
    "Age": [20,18,19,20],
    "Marks": [74,83,93,84],
    "Grade": ["C","B","A","B"],
    "City": ["Surat", "Morbi", "Navsari", "Mehsana"]
}

df= pd.DataFrame(data)
print(df)

# using .drop
# df.drop(columns = "Col_Name", inplace = True)
# if inplace=True, modifies the df
# False, returns a new df
df.drop(columns= ["City"], inplace = True)
print(df)
