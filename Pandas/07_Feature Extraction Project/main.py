import pandas as pd
import numpy as np

df = pd.read_csv('anime.csv')

print(df.head())

# 1. Extract episode counts
def extract_episodes(txt):
    check = False
    data = ''
    for i in txt:
        if i == ')':
            check = False
            return data
        if check == True:
            data += i
        if i == '(':
            check = True

df['Episodes'] = df['Title'].apply(extract_episodes)
print(df.head())

# now I want only int part of episodes
df['Episodes'] = df['Episodes'].str.replace(' eps','') #removing ' eps' from the string
df['Episodes'] = df['Episodes'].astype(int) # converting the datatype to int
print(df.head())

# 2. Extract timestamp
def extract_timestamp(txt):
    data = ''

    for i in range(len(txt)):
        if txt[i] == ')':
            check = True
            for j in range(i+1,i+20):
                data += txt[j]
    return data

df['Timestamp'] = df['Title'].apply(extract_timestamp)
print(df.head())

# 3. Extract time duration
def extract_duration(ts):
    start = ''
    end = ''
    dash_seen = False

    # manually parse start & end parts
    for ch in ts:
        if ch == '-':
            dash_seen = True
            continue

        if not dash_seen:
            start += ch
        else:
            end += ch

    # clean spaces
    start = start.strip()
    end = end.strip()

    # convert to datetime
    start_dt = pd.to_datetime(start, format="%b %Y")
    end_dt = pd.to_datetime(end, format="%b %Y")

    # calculate months
    months = (end_dt.year - start_dt.year) * 12 + \
             (end_dt.month - start_dt.month)

    return months
df['Duration (Months)'] = df['Timestamp'].apply(extract_duration)
print(df.head())

# 4. Which anime has the highest score
print(df[df['Score']==df['Score'].max()][['Title','Score']])

# 5. give me top 5 highest scoring anime
print(df.sort_values(by='Score', ascending=False).head(5)[['Title', 'Score']])

# 6. which anime has the highest episode count
print(df[df['Episodes']==df['Episodes'].max()][['Title', 'Episodes']])

# 7. animes with top 5 episode count
print(df.sort_values(by='Episodes', ascending=False).head()[['Title', 'Episodes']])

# 8. which is the longest running anime
print(df[df['Duration (Months)']==df['Duration (Months)'].max()][['Title', 'Duration (Months)']])

