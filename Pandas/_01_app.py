import pandas as pd

# read data - csv, json, excel
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
print(df)

# df = pd.read_excel("SampleSuperstore.xlsx")
# df = pd.read_json("sample_Data.json")

# crate dataFrame from dictionary
data ={
    "Name":["Harsh","Pujan","Krips","Bhavy","Divy"],
    "Marks":[74,83,999,73,93],
    "City":["Surat","Morbi","Navsari","Mahesana","Surendranagar"]
}

df = pd.DataFrame(data)
print(df)

# to save dataframe as csv, json, excel
# df.to_csv("output.csv")
# df.to_json("output.json")
df.to_excel("output.xlsx", index = False)