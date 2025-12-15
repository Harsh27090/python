# to get statistical analysis 
import pandas as pd

# step1 - create dataframe
data ={
    "Name":["Harsh","Pujan","Krips","Bhavy","Divy"],
    "Marks":[74,83,999,73,93],
    "City":["Surat","Morbi","Navsari","Mahesana","Surendranagar"],
    "Scholarship":[32000,85000,92000,74000,92000]
}

df = pd.DataFrame(data)
print(df.describe())

