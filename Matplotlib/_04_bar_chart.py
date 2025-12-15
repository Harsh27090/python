"""
plt.bar(x, y, height='', color='', label='')
"""

import matplotlib.pyplot as plt

product = ['A','B','C','D']
sales = [1000,1500,1200,2200]

plt.bar(product,sales, color='orange', label='product sales')

plt.title("Product sales 2025")
plt.xlabel('Product')
plt.ylabel('Sales')
plt.legend('Sales 2025')
plt.show()