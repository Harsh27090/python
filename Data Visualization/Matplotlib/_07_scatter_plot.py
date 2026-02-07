"""
plt.scatter(x,y, color='', marker='', label='')
"""
import matplotlib.pyplot as plt

hours = [1,2,3,4,5,6,7,8]
marks = [50,60,70,77,80,82,83,81]

plt.scatter(hours, marks, color='orange', marker='D', label='marks relationship')
plt.title('Relationship between marks and hours studied')
plt.xlabel('Hours studied')
plt.ylabel('Marks scored')
plt.grid(color='gray')
plt.show()

# find co-relationship between two variables, like sales vs advertising, temp. vs icecream sales