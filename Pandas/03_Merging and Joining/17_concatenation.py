"""
"cross join"
.concat([df1, df2], axis=0/1, ignore_index=True/False)
stack two dataframes
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

df_concat = pd.concat([df_cname, df_amt], axis=0, ignore_index=True)
print(df_concat)