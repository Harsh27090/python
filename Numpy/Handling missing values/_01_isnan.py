"""
.isnan(array)
"""
import numpy as np
arr1 = np.array([10,20,np.nan,40])
print(np.isnan(arr1))

# we cannot compare two missing values