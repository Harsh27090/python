"""
np.isnan(array, nan=value)
"""
import numpy as np
arr1 = np.array([10,20,np.nan,40, np.nan,60,70])

clean_arr = np.nan_to_num(arr1,nan=1)
print(clean_arr)
