"""
no. of rows and columns?
no. elements?

"""

import numpy as np
arr = np.array([[10,20.6,30],[40,50,60]])

print(arr)
print(arr.shape) #(rows, cols)
print(arr.size) # total no. of elements
print(arr.ndim) # no. of dimensions
print(arr.dtype) # datatype of elements
print(arr.astype(int))