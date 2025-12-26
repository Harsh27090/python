import pandas as pd

import pandas as pd
data1 = {
    "CID": [1,2,3],
    "CName": ["Harsh", "Pujan", "Krips"]
}
df_cname = pd.DataFrame(data1)
df_cname = df_cname.set_index("CID")
data2 = {
    "CID": [1,2,4],
    "Amt": [349,834,643]
}
df_amt = pd.DataFrame(data2)
df_amt = df_amt.set_index("CID")

df_join = df_cname.join(df_amt, how='outer')
print(df_join)