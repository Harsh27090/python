# map - applies a function to each element of a list
# it can apply both lambda and normal function
# it returns an object
a = [1,2,3,4,5]

doubled = map(lambda x: x*2,a)
print(doubled)
print(list(doubled))


def double(x):
    return x*2
doubled1 = map(double,a)
print(doubled1)
print(list(doubled1))

# filter - it is used to filter out elements from a list
# it returns an object
# it works on boolean values, it filter outs the "True" values
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

even = filter(lambda x: True if x%2==0 else False,b)
print(even)
print(list(even))

