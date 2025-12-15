import math

x = 7
y = 2
z = 1 + 2j

print(x + y)
print(x - y)
print(x * y)
print(x / y) # float value
print( x // y) # integer value
print(x % y)
print(x ** y) # exponential

x += 3.32
print(x)
print(round(x)) # rounds the no.
print(abs(x)) # absolute val. (|x|)
print(math.ceil(x))
print(math.floor(x))

x = input("x = ")
y = float(x) + 4 # type conversion
print(y)