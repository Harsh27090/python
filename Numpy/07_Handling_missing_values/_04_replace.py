import numpy as np
arr1 = np.array([10,20,np.inf,40, -np.inf])

print(np.isinf(arr1))
clean_arr = np.nan_to_num(arr1, posinf=1000, neginf=-1000)
print(clean_arr)