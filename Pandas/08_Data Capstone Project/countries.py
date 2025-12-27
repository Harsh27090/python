import pandas as pd
import numpy as np
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 2000)
pd.set_option("display.max_colwidth", None)

df = pd.read_csv('countries.csv')

print(df.head())
print(df.columns)

# 1. which country has the highest population
print(f'1.\n{df[df['population']==df['population'].max()][['country','population']]}\n')

# 2. capital of the country with the highest population
print(f'2.\n{df[df['population']==df['population'].max()][['country','capital_city','population']]}\n')

# 3. which country has the least population
print(f'3.\n{df[df['population']==df['population'].min()][['country','population']]}\n')

# 4. capital of the country with the least population
print(f'4.\n{df[df['population']==df['population'].min()][['country','capital_city','population']]}\n')

# 5. top 5 countries with the highest democratic score
print(f'5.\n{df.sort_values(by='democracy_score').head()}\n')

# 6. how many total regions are there
print(f'6.\n{len(df['region'].unique())}\n')

# 7. no. of countries in Eastern Europe region
print(f'7.\n{len(df[df['region']=='Eastern Europe'])}\n')

# 8. who is the political leader 2nd most populated country
# print(f'8.\n{df.sort_values(by='population', ascending=False).iloc[1][['country','political_leader']]}\n')
print(f'8.\n{df[df['population']==df['population'].nlargest(2).iloc[1]][['country','political_leader']]}\n')

# 9. no. of countries that contain "Republic" in their name
print(f'9.\n{len(df[df['country_long'].str.contains('republic', case=False)])}\n')

# 10. which country in the african region has the highest population
print(f'10.\n{df[df['continent']=='Africa'].sort_values(by='population', ascending=False).head(1)[['country','population']]}\n')