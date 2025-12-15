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

