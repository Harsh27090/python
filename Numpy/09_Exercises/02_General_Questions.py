import numpy as np
# Columns: [Age, Math Marks, Science Marks]
data = np.array([
    [18, 85, 78],   # Student 1
    [19, 92, 88],   # Student 2
    [17, 76, 95],   # Student 3
    [18, 65, 70],   # Student 4
    [20, 90, 85]    # Student 5
])

# 1. Get the shape of the matrix.
print(data.shape)

# 2. Find the average age of students.
print(np.mean(data[:,0]))

# 3. Extract Math marks of all students.
print(data[:,1])

# 4. Find the highest Science mark.
print(np.max(data[:,2]))

# 5. Get details of the student who scored more than 90 in Math.
print(data[data[:,1]>90])

# 6. Increase Math marks of all students by 5.
data[:,1] += 5
print(data)

# 7. Find how many students are younger than 19.
print(len(data[data[:,0]<19])) # len returns size of the first element
# arr = data[data[:,0]<19]
# print(arr[:,0].size) # size returns the total no. of elements

# 8. Calculate the average marks in each subject (column-wise mean).
print(np.mean(data[:,1:3]))
# print(np.mean(arr_mean, axis=0))

# 9. Get data of students who scored at least 80 in both subjects.
print(data[(data[:,1]>80) & (data[:,2]>80)])

# 10. Replace all Science marks < 75 with 0.
data[:,2][data[:,2]<75] = 0
print(data)