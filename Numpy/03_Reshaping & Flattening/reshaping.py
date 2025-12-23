""""
changing the dimension of an array without modifying the data
reshape(rows,cols)
- possible only if the size matches
- returns a copy, not modifying og array
"""
import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr.reshape(2,3))