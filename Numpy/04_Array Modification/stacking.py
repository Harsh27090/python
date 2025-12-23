"""
stacking multiple arrays into one
vertically or horizontally

vstack() - row wise - merges two arrays
hstack((arr1,arr2,...)) - column wise - joins to arrays
"""
import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
arr3 = np.array([11,12,13,14,15])

new_arr1= np.hstack((arr1,arr2,arr3))
print(f'hstack: \n{new_arr1}')
print(f'vstack: \nb {np.vstack((arr1,arr2, arr3))}')

arr4 = np.array([[1,2],[3,4]])
arr5 = np.array([[5,6],[7,8]])
new_arr2 = np.vstack((arr4,arr5))
print(new_arr2)
print(np.hstack((arr4,arr5)))