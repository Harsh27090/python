python_list = [1,2,3,4,5]
print(python_list)

import numpy as np
print("1d array:")
numpy_array = np.array([1,2,3,4,5])
print(numpy_array)
print("2d array:")
numpy_2d = np.array([[1,2,3],
                    [4,5,6]])
print(numpy_2d)
print("Multidimensional array (Matrix):")
numpy_multidm = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [11,12,13]
    ]
])
print(numpy_multidm)
print()

# fill by default value

# zeros -> fill each by 0
# pd.zeros(shape)
# 1d->(m), 2d-> (m,n), multi->(m,n,...)
numpy_zeros = np.zeros((2,2))
print(numpy_zeros)
print()

# ones -> fill by 1
# pd.ones(shape)
numpy_ones = np.ones((2,2))
print(numpy_ones)
print()

# fill with provided value
# full(shape, val)
filled_arr = np.full((2,3),7)
print(filled_arr)
print()

# arange(start,stop,step) -> similar to range
arange_arr = np.arange(1,10,2)
print(arange_arr)
print()

#creating identity matrix
# eye(shape)
identity_matrix = np.eye(3)
print(identity_matrix)