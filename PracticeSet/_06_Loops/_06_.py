# factorial of a given no.

num = int(input('Enter a number: '))
fact = 1
if num==0 or num==1:
    fact = 1

else:
    for i in range(num,0,-1):
        fact *= i

print(f'The factorial of {num} is {fact}')