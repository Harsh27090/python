# 1. importing necessary libraries
import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 2000)
pd.set_option("display.max_colwidth", None)

# 2. loading dataset
df = pd.read_csv("student_admission_record_dirty.csv")
print(df.head())

# 3. check missing values
print("Missing values in each column:")
print(df.isnull().sum())
print(df.iloc[0])

# 4. replacing numerical missing values with their mean/median
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Admission Test Score'] = df['Admission Test Score'].fillna(df['Admission Test Score'].mean())
df['High School Percentage'] = df['High School Percentage'].interpolate(method='linear')
print(df.isna().sum())

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.drop_duplicates(inplace=True)
print(df.isna().sum())

# replacing negative values

# ........... incomplete