import numpy as np
arr = np.array([1,2,3,4,5])
print(arr[2])
print(arr[-2])
# print(arr[10])

arr_2d = np.arange(1,31).reshape(6,5)
print(arr_2d)
print(arr_2d[1])
print(arr_2d[0:2,1:3])
print(arr_2d[3:,3:])

# boolean indexing
arr1 = np.arange(1,21)
print(arr1)
bool_idx = arr1%2 == 0
arr1 = arr1[bool_idx]
print(arr1)