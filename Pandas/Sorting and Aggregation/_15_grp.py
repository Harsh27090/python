import pandas as pd

data={
    "Name": ["Harsh", "Pujan", "Krips", "Bhavy", "Divy"],
    "Age": [20,18,19,20,19],
    "Salary": [38000,45000,50000,40000,69000]
}
df=pd.DataFrame(data)
grp = df.groupby("Age")["Salary"].sum()
print(grp)

grp2 = df.groupby(["Age", "Name"])["Salary"].sum()
print(grp2)

"""
sum()
min()
max()
mean()
std()
count()
"""
