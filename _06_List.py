# creation
# 1
my_list = [1,2,[3,3,3],4,5,'Harsh',True,False,6,7,8,9]
print(my_list)

# 2. using list constructor
my_list2 = list((1,2,3,4,5,'Harsh',True,False,6,7,8,9))
print(my_list2)

# access
print(my_list[2])

# update
# 1.
my_list[2] = 3
print(my_list)
# 2. using slicing
my_list[8:] = 0,0,0,0
print(my_list)

# concatenate
result = my_list + my_list2
print(result)

# repetition
print(my_list * 2)

# membership
print('Harsh' in my_list)
print('Python' not in my_list)


