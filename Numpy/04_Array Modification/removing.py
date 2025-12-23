"""
np.delete(arr, index_no, axis)
"""

import numpy as np
arr1 = np.array([1,2,3,4,5])
print(arr1)
new_arr1 = np.delete(arr1, 3)
print(new_arr1)

arr2 = np.array([[1,2],[3,4],[5,6]])
print(arr2)
new_arr2 = np.delete(arr2, 1, axis=1)
print(new_arr2)