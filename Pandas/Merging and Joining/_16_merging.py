"""
merged = pd.merge(df1, df2, on="col_name", how="join_type")
inner,outer,left,right,cross
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

merged1 = pd.merge(df_cname, df_amt, on="CID", how="inner")
print(merged1)
# print()
merged1 = pd.merge(df_cname, df_amt, on="CID", how="outer")
print(merged1)
print()
merged1 = pd.merge(df_cname, df_amt, on="CID", how="left")
print(merged1)
print()
merged1 = pd.merge(df_cname, df_amt, on="CID", how="right")
print(merged1)
print()
