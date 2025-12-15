"""
.ravel() -> modify
.flatten() -> does not modify
"""

import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr.ravel())
print(arr.flatten())

# used when there are multiple dimensions, and you want to see the data in a single row