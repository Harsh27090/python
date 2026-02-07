"""
savefig('filename.extension', dpi= ,bbox_inches='tight')
"""

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,15,13,18]

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('plot title')

plt.savefig('linechart.png', dpi=100, bbox_inches='tight') # save before show()
plt.show()