# info()

# 1. no. of rows and cols
# 2. col names
# 3. data types of objects
# 4. non-null counts
# 5. memory usage by df

import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
print(df.info())