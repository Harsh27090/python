import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = sns.load_dataset('tips')

sns.countplot(x='sex', data=df, hue='smoker')
plt.show()

sns.barplot(x=df['sex'], y=df['total_bill'],estimator=np.sum)
plt.show()

sns.boxplot(x='day', y='tip', data=df)
plt.show()

sns.violinplot(x='day', y='tip', data=df)
plt.show()

# stripplot: similar to boxplot but with scatter
sns.stripplot(x='day', y='tip', data=df)
plt.show()

# swarmplot: similar to violinplot but with scatter
sns.swarmplot(x='day', y='tip', data=df)
plt.show()

# combining violinplot and swarmplot
sns.violinplot(x='day', y='tip', data=df)
sns.swarmplot(x='day', y='tip', data=df)
plt.show()