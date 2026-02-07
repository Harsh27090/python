"""
plt.hist(values, bins=no_of_bins, color='', edgecolor='')
"""

import matplotlib.pyplot as plt

scores = [40,49,84,64,89,64,92,74,45,92,83,38,65,23,65,86,34,76,73,93,92,67,59,53,52]

plt.hist(scores, bins=7, color='green', edgecolor='black', label='Scores of students')
plt.title('Score distribution of students')
plt.xlabel('Scores')
plt.ylabel('No. of Students')
plt.show()

# height of bar = no. of students (frequency)