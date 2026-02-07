import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
# x: data using which you want to predict, y: data which you want to predict
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers = ['o','x'])
plt.show()