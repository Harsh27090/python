"""
np.insert(array, index, value, axis)
returns a new array
"""
import numpy as np

arr1 = np.array([1,2,3,4,5])
print(arr1)
new_arr1=np.insert(arr1, 1, 8, axis=0)
print(new_arr1)

arr2=np.array([[1,2],[3,4]])
print(arr2)
new_arr2=np.insert(arr2, 1,[5,6], axis=1)
print(new_arr2)
