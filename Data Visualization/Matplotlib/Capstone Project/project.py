import pandas as pd
import matplotlib.pyplot as plt

# 1. load the data
df = pd.read_csv('netflix_titles.csv')
print(df.head())

# 2. clean the data
df.dropna(subset=['type', 'release_year', 'country', 'rating', 'duration'])

# 3.

# 4.
type_counts = df['type'].value_counts()
plt.figure(figsize=[10,5])
plt.bar(type_counts.index, type_counts.values, color=['red', 'green'])
plt.title('Movies vs TV Shows')
plt.xlabel('Type')
plt.ylabel('Count')
plt.savefig('movies_vs_tvshows.png', dpi=100, bbox_inches='tight')
plt.show()

