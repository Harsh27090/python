import numpy as np
m1 = np.array([[1,2],
              [3,4]])
m2 = np.array([[1,2],
              [3,4]])

print(f'm1:\n{m1} \n m2:\n{m2}')
ans = m1 * m2 # it just multiplies by index
print(f'Wrong multiplication:\n{ans}')

matrix_mul = m1 @ m2
# np.dot(m1,m2)
print(f'Matrix multiplication:\n{matrix_mul}')

# transpose
print(m1.T)
print(np.transpose(m1))
