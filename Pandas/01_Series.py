import pandas as pd
import numpy as np

labels = ['a', 'b', 'c', 'd', 'e']
list1 = [1,2,3,4,5]
arr1 = np.array(list1)
dict = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5
}
s1 = pd.Series(list1)
s2 = pd.Series(list1, index=labels)
s3 = pd.Series(arr1, index=labels)
s4 = pd.Series(dict)

print(s1)
print(s2)
print(s3)
print(s4)
