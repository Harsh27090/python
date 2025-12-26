import pandas as pd

data = {
    "Name": ["Harsh", "Pujan", "Krips", "Bhavy"],
    "Age": [21, 22, 20, 23],
    "City": ["Delhi", "Mumbai", "Pune", "Delhi"]
}

df = pd.DataFrame(data)

# 1. print first 3 rows
print(f'1.\n{df.head(3)}\n')

# 2. Get list of column names
print(f'2.\n{df.columns}\n')

# 3. Show summary statistics
print(f'3.\n{df.describe()}\n')

# 4. Select rows where Age > 21
print(f'4.\n{df[df['Age']>21]}\n')

# 5. Select only Name & City columns
print(f'5.\n{df[['Name','City']]}\n')

# 6. Count number of rows
print(f'6.\n{len(df)}\n')


marks = {
    "Name": ["Harsh", "Pujan", "Bhavy", "Krips"],
    "Maths": [80, 92, None, 75],
    "Science": [88, 85, 91, None]
}
df2 = pd.DataFrame(marks)

# 7. Check missing values
print(f'7.\n{df2.isna()}\n')

# 8. Fill missing values with column mean
df2['Maths'] = df2['Maths'].fillna(df2['Maths'].mean())
df2['Science'] = df2['Science'].fillna(df2['Science'].mean())
print(f'8.\n{df2}\n')

# 9. Sort rows by Maths in descending order
print(f'9.\n{df2.sort_values(by=['Maths'],ascending=False)}\n')

# 10. Add a new column “Total” = Maths + Science
df2['Total'] = df2['Maths'] + df2['Science']
print(f'10.\n{df2}\n')



