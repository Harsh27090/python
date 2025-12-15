# greatest of 4 nos.
a1 = int(input('Enter a no.:'))
a2 = int(input('Enter a no.:'))
a3 = int(input('Enter a no.:'))
a4 = int(input('Enter a no.:'))

if a1>a2 and a1>a3 and a1>a4:
    print('greatest is a1:', a1)

elif a2>a1 and a2>a3 and a2>a4:
    print('greatest is a2:', a2)

elif a3>a1 and a3>a2 and a3>a4:
    print('greatest is a1:', a3)

else:
    print('greatest is a1:', a4)


