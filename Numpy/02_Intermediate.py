import numpy as np

# 1. Create a 6×6 matrix and extract the border elements only
arr1 = np.arange(1,37).reshape(6,6)
print(f'arr1:\n{arr1}')
border = np.concatenate([
    arr1[0,:],
    arr1[-1,:],
    arr1[1:-1,0],
    arr1[1:-1,-1]
])
print(f'border:\n{border}')

# 2. Select all rows where the second column is greater than 50.
arr2 = np.array([
    [1, 45, 78],
    [2, 52, 67],
    [3, 88, 90],
    [4, 33, 40],
    [5, 60, 82],
    [6, 49, 55]
])
print(f'Q2:\n{arr2[arr2[:,1]>50]}')

# 3. Count how many elements are greater than the mean value.
arr3 = np.array([12, 25, 37, 18, 42, 30, 55, 10, 48])
print(np.mean(arr3))
print(f'Q3:\n{np.sum([arr3>np.mean(arr3)])}')

# 4. Sort by last column
arr4 = np.random.randint(1,31, (5,6))
print(f'arr4:\n{arr4}')
order = np.argsort(arr4[:,-1])
print(f'arr4(Sorted by last column):\n{arr4[order]}')


