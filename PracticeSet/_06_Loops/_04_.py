# prime or not

num = int(input("Enter a number: "))

if num<1:
    print('Not valid')

else:
    for i in range(2,num):
        if num%i==0:
            print('not a prime no.')
            break
    else:
        print('Prime')
