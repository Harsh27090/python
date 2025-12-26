import pandas as pd

data = {
    "Name": ["Harsh", "Pujan", "Krips", "Bhavy"],
    "Age": [21, 21, 20, 23],
    "City": ["Delhi", "Mumbai", "Pune", "Delhi"]
}

df = pd.DataFrame(data)
marks = {
    "Name": ["Harsh", "Pujan", "Bhavy", "Krips"],
    "Maths": [80, 92, None, 75],
    "Science": [88, 85, 91, None]
}
df2 = pd.DataFrame(marks)

# 1. Filter students scoring > 85 in BOTH subjects
print(f'1.\n{df2[(df2['Maths']>80) & (df2['Science']>80)]}\n')

# 2. Group by City & find average age
print(f'2.\n{df.groupby(by='City')['Age'].mean()}\n')

# 3. Count number of students in each city
print(f'3.\n{df.groupby(by='City').size()}\n')

# 4. Rename column “City” to “Location”
print(f'4.\n{df.rename(columns={'City': 'Location'})}\n')

df_student = pd.DataFrame({
    "ID": [1,2,3],
    "Name": ["Harsh","Pujan","Krips"]
})

df_score = pd.DataFrame({
    "ID": [1,2,3],
    "Score": [88, 92, 75]
})
# 5. Merge student info & marks
merged = pd.merge(df_student, df_score, on='ID')
print(f'5.\n{merged}\n')

# 6. Replace city “Delhi” with “New Delhi”
print(f'6.\n{df.replace('Delhi','New Delhi')}\n')

# 7. Sort DataFrame by two columns
print(f'7.\n{df2.sort_values(by=['Maths','Science'])}\n')

# 8. Select top 2 students by Maths marks
print(f'8.\n{df2.sort_values(by='Maths', ascending=False).head(2)}\n')

# 9. Convert Age column into category dtype
df['Age'] = df['Age'].astype('category')
print(f'5.\n{df}\n')
print(f'{df['Age']}')


