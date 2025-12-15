# head(), tail(),  -> 5
# head(n), tail(n) -> n

import pandas as pd

df=pd.read_csv("sales_data_sample.csv", encoding="latin1")
print(df.head())
print(df.tail(3))