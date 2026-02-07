import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 2000)
pd.set_option("display.max_colwidth", None)

df = pd.read_csv('IPL.csv')

# basic info
print(df.info())

# no. of rows and columns
print(f'no. of rows: {df.shape[0]}\nno. of columns: {df.shape[1]}')

# null values
print(df.isnull().sum())

# 1. which team won the most matches?
print(f'\n1. Team with most wins: {df['match_winner'].value_counts().idxmax()}\n')
match_wins = df['match_winner'].value_counts()
sns.barplot(x=match_wins.values, y=match_wins.index)
plt.title('Match wins by each team')
plt.show()

# 2. Toss Decision Trends
sns.countplot(x=df['toss_decision'])
plt.title('Toss decision trend')
plt.show()

# 3. toss winner vs match winner : calculate percentage of winning the match after winning the toss
count = df[df['toss_winner']==df['match_winner']]['match_id'].count()
percentage = (count*100)/df.shape[0]
print(f'3. Percentage of winning the match after winning the toss: {percentage.round(2)}')

# 4. how do teams win? (runs vs wicket)
sns.countplot(df, x='won_by')
plt.show()

# 5. Most 'player of the match' awards
potm = df['player_of_the_match'].value_counts().head(10)
print(potm.idxmax())
sns.barplot(x=potm.values, y=potm.index, palette='rainbow')
plt.show()
print(df.head())

# 6. 
