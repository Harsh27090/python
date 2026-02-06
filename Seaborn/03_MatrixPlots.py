import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

print(tips.head())
print(flights.head())

tipscorr = tips[['total_bill', 'tip', 'size']]

# heatmap
sns.heatmap(tipscorr.corr(), annot=True)
plt.show()

# clustermap
sns.clustermap(tipscorr.corr())
plt.show()

# heatmap with pivot table
flightspvt = flights.pivot_table(values = 'passengers', index = 'month', columns='year')

print(flightspvt.head())
sns.heatmap(flightspvt)
plt.show()
