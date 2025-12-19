# 1. list comprehension

squares = [x**2 for x in range(1,11)]
print(squares)

# 2. set comprehension

divisors = {x for x in range(1,11) if 105%x==0}
print(divisors)

# 3. dictionary comprehension

cubes = {x:x**3 for x in range(1,5)}
print(cubes)