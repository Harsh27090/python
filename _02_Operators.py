x = 42
y = 48

# Conditional Operators :
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x == y)
print(x != y)

# Ternary Operator :
age = 18
message = "Valid" if age >= 18 else "Invalid"
print(message)

# Logical Operators : and, or, not
high_income = True
good_credit = False
student = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")

if high_income or good_credit:
    print("Eligible")
else:
    print("Not Eligible")

if not student:
    print("Eligible")
else:
    print("Not Eligible")

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")

# for "and", evaluation stops if false is found, as 1 false results in false
# for "or", evaluation stops if true is found, as 1 true results in true

# chaining comparison operators
if 18 <= age < 60:
    print("Eligible")
else:
    print("Not Eligible")

# identity operator
# is
# is not
a = [1,2,3]
b = a
c = [1,2,3]
print(a is b)
print(a is c)

str1 = "Python is fun"
print("fun" in str1)