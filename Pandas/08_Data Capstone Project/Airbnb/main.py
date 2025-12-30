import numpy as np
import pandas as pd

df = pd.read_csv('Airbnb_Open_Data.csv')

print(df.info())
print(df.isnull().sum())