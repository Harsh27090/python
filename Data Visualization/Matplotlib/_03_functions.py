"""
plt.plot(x, y, color=' ', linestyle=' ', linewidth=' ', marker=' ', label=' ')
plt.xlabel('label for x-axis')
plt.ylabel('label for y-axis')
plt.title('')
plt.legend(loc='upper left/ lower right', fontsize='')
plt.grid(color='', linestyle='', linewidth='')
plt.xlim(lower_limit, upper_limit)
plt.ylim(lower_limit, upper_limit)
plt.xticks([1,2,3,4], ['M1','M2','M3',"M4"])
plt.yticks([1000,1500,1200,1800], ['','','',''])
plt.show()
"""

import matplotlib.pyplot as plt

months = [1,2,3,4]
sales = [1000,1500,1200,1800]

plt.plot(months, sales, color='green', linestyle='--', linewidth=2, marker='o', label='2025 sales data')

plt.title("Sales of 2025")

plt.xlabel('Months')
plt.ylabel('Sales per month')

plt.legend(loc='upper left', fontsize='10')

plt.grid(color='gray', linestyle=':', linewidth='1')

plt.xlim(1,5)
plt.ylim(1000,2000)

plt.xticks([1,2,3,4], ['M1', 'M2', 'M3', 'M4'])

plt.annotate('Peak Value', xy=(4,1800), xytext=(3,1800), arrowprops=dict(arrowstyle='->'))

plt.show()
