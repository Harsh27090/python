import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 2000)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.max_rows", None)

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
plt.title('1.Match wins by each team')
plt.show()

# 2. Toss Decision Trends
sns.countplot(x=df['toss_decision'])
plt.title('2.Toss decision trend')
plt.show()

# 3. toss winner vs match winner : calculate percentage of winning the match after winning the toss
count = df[df['toss_winner']==df['match_winner']]['match_id'].count()
percentage = (count*100)/df.shape[0]
print(f'3. Percentage of winning the match after winning the toss: {percentage.round(2)}')

# 4. how do teams win? (runs vs wicket)
sns.countplot(df, x='won_by')
plt.title('4.Runs vs Wickets')
plt.show()

# 5. Most 'player of the match' awards
potm = df['player_of_the_match'].value_counts().head(10)
print(f'5. Most player of the match:\n{potm.idxmax()}')
sns.barplot(x=potm.values, y=potm.index, palette='rainbow')
plt.title('5. Most player of the match awards')
plt.show()

# 6. 2 top scorers
top_scorer = df.groupby('top_scorer')['highscore'].sum()
print(f'6. 2 top scorers:\n{top_scorer.sort_values(ascending=False).head(2)}')
sns.barplot(x=top_scorer.values, y=top_scorer.index)
plt.title('6. 2 top scorers')
plt.show()


# 7. 10 best bowling figures
df['highest_wickets'] = df['best_bowling_figure'].apply(lambda x:x.split('--')[0])
df['highest_wickets'] = df['highest_wickets'].astype(int)
top_bowl = df.groupby('best_bowling')['highest_wickets'].sum().sort_values(ascending=False).head(10)
print(f'7. 10 best bowling figures:\n{top_bowl}')
sns.barplot(x=top_bowl.values, y=top_bowl.index)
plt.title('7. 10 best bowling figures')
plt.show()

# 8. most matches played by venue
venues = df['venue'].value_counts()
sns.barplot(x=venues.values, y=venues.index)
plt.title('8. Most matches played by venue')
plt.show()

# 9. who won with the highest margin by runs
margin_runs = df[df['won_by']=='Runs'].sort_values(by='margin' ,ascending=False)[['match_winner', 'margin']]
print(margin_runs.head(10))

# 10. player with the highest individual score
print(f'10. Player with the highest individual score:\n{df[df['highscore']==df['highscore'].max()][['top_scorer', 'highscore']]}')

# 11. bowler with best bowling figure
print(f'11. Bowler with best bowling figure:\n{df[df['highest_wickets']==df['highest_wickets'].max()][['best_bowling','best_bowling_figure', 'highest_wickets']]}')

print(df.head())
