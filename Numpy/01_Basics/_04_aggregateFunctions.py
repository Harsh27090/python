"""
np.sum()
np.mean(arr)
np.min(arr)
np.max(arr)
.std
.var
np.function() can take axis=0/1
arr.function() cannot take axis=0/1, it performs action as an array as whole
"""
import numpy as np
arr = np.array([[10,20,30],
                [40,50,60],
                [70,80,90]])
print(arr.sum())
print(np.sum(arr, axis=0))
# print(np.sum(arr, axis=1))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
print(np.std(arr))
print(np.var(arr))
print(np.median(arr))



