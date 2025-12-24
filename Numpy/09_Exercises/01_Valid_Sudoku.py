import numpy as np
s = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],

    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],

    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
])

s_rows = False
sum_rows = np.sum(s, axis=1)
for i in sum_rows:
    if i != 45:
        print('Sudoku not valid!')
        break
else:
    s_rows = True
    print('Sudoku valid for rows!')

s_cols = False
sum_cols = np.sum(s,axis=0)
for i in sum_cols:
    if i != 45:
        print('Sudoku not valid!')
        break
else:
    s_cols = True
    print('Sudoko valid for columns!')

sum_blocks = np.array([
    s[i:i+3,j:j+3].sum() for i in range(0,9,3) for j in range(0,9,3)
])

s_blocks=False
for i in range(0,9,3):
    for j in range(0,9,3):
        sum_block = s[i:i+3,j:j+3].sum()
        if sum_block != 45:
            print('Sudoku not valid!')
            break
else:
    s_blocks = True
    print('Sudoku valid for blocks!')

# for block in sum_blocks:
#     if block != 45:
#         print('Sudoku not valid!')
#         break
# else:
#     print('Sudoku valid!')

if s_rows == s_cols == s_blocks == True:
    print('Sudoku valid!')
else:
    print('Sudoku not valid!')




