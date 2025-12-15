"""
multiple charts in one window
saves space
good for comparison
plt.subplot(row, col, index)

functions
plt.subplot(nrows, ncols,index)
plt.subplots(nrows, ncols, figsize=(width, height)
plt.tight_layout()
ax.plot()
ax.set_title
"""

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,15,20,18,25]

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title('Line Graph')

plt.subplot(1,2,2)
plt.bar(x,y)
plt.title('Bar Chart')

plt.show()