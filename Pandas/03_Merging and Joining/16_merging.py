"""
merged = pd.merge(df1, df2, on="col_name", how="join_type")
inner,outer,left,right
"""
import pandas as pd
data1 = {
    "CID": [1,2,3],
    "CName": ["Harsh", "Pujan", "Krips"]
}
df_cname = pd.DataFrame(data1)
data2 = {
    "CID": [1,2,4],
    "Amt": [349,834,643]
}
df_amt = pd.DataFrame(data2)

merged1 = pd.merge(df_cname, df_amt, on="CID", how="inner") # common in both
print(merged1)
# print()
merged1 = pd.merge(df_cname, df_amt, on="CID", how="outer") # all data, fills missing with nan
print(merged1)
print()
merged1 = pd.merge(df_cname, df_amt, on="CID", how="left") # all data from left
print(merged1)
print()
merged1 = pd.merge(df_cname, df_amt, on="CID", how="right") # all data from right
print(merged1)
print()
