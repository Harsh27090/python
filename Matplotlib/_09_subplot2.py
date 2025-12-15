"""
fig, ax = plt.subplots(nrows, ncols, figsize=(width, height))
"""

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,15,13,18]

fig, ax = plt.subplots(1,2, figsize=(10,5))

ax[0].plot(x,y)
ax[0].set_title('Line Graph')

ax[1].bar(x,y)
ax[1].set_title('Bar Chart')

fig.suptitle('Comparison of Line and Bar Chart')
plt.tight_layout() # adjust the layout
plt.show()