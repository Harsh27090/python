# name in list or not

names = ['harsh', 'pujan', 'shyam', 'krips', 'utsav', 'divy', 'bhavy']

username = input('Enter your name: ')

if username.lower() in names:
    print('in the list')

else:
    print('not in list')