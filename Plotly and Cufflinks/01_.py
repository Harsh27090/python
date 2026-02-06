import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

tips = sns.load_dataset('tips')

fig = px.line(tips, y='total_bill')
fig.show()

fig2 = px.histogram(tips, x='total_bill', nbins=20)
fig2.show()

fig3 = px.box(tips, x='day', y='tip')
fig3.show()

fig4 = px.scatter(tips, x='total_bill', y='tip', trendline='ols')
fig4.show()