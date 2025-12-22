# 1. importing necessary libraries
import pandas as pd
import numpy as np

# 2. loading dataset
df = pd.read_csv("student_admission_record_dirty.csv")
print(df.head())

# 3. check missing values
print("Missing values in each column:")
print(df.isnull().sum())

# ............incomplete