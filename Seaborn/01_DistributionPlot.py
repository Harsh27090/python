import seaborn as sns
import matplotlib.pyplot as plt
print(sns.get_dataset_names())

df = sns.load_dataset('tips')

plt.subplot(1,2,1)
sns.histplot(df['total_bill'])
# plt.show()

plt.subplot(1,2,2)
sns.histplot(df['tip'])
# plt.show()
plt.show()

sns.jointplot(x='total_bill', y='tip', data=df, kind='reg')
plt.show()

sns.pairplot(df, hue='sex')
plt.show()

sns.rugplot(df)
plt.show()

sns.rugplot(df['total_bill'])
plt.show()

