import numpy as np
import random

# 1. Create a NumPy array of numbers from 10 to 30
arr1 = np.arange(10,31)
print(f'arr1:\n{arr1}')

# 2. Create a 4×4 matrix of zeros and change the diagonal to 5.
arr2 = np.zeros((4,4))
np.fill_diagonal(arr2,5)
print(f'arr2:\n{arr2}')

# 3. Create an array of 20 random integers between 1 and 100.
arr3 = np.random.randint(10,101,20)
print(f'arr3:\n{arr3}')

# 4. Convert a Python list to a NumPy array and print its - shape, size, data type
list1 = [
    [1,2,3],
    [4,5,6]
]
arr4 = np.array(list1)
print(f'arr4:\n{arr4}')
print(f'Shape of arr4: {arr4.shape}')
print(f'Size of arr4: {arr4.size}')
print(f'Data type of arr4: {arr4.dtype}')

# 5. Replace all even numbers with −1 in an array.
arr5 = np.arange(0,21)
bool_index = arr5%2==0
arr5[bool_index] = -1
print(f'arr5:\n{arr5}')

