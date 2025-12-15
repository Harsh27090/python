# sum of first n natural nos.

num = int(input('Enter a number: '))
sum1 = 0

for i in range(1,num+1):
    sum1 += i

print(f'The sum of first {num} natural nos. is {sum1}')
