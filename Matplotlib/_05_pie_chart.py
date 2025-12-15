"""
plt.pie(values, labels=label_list, colors=colors_list, autopct='%1.1f%%')
"""

import matplotlib.pyplot as plt

revenues = [10000,15000,30000,21000]
regions = ['East','West','North', 'South']

plt.pie(revenues, labels=regions, colors=[' pink','lightblue','green','orange'], autopct='%1.1f%%')
plt.title('Revenues of regions')
plt.show()