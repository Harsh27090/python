# pass if all 40% and 33% each
marks1 = float(input('Enter marks1: '))
marks2 = float(input('Enter marks2: '))
marks3 = float(input('Enter marks3: '))

avg = (marks1 + marks2 + marks3) / 3

if marks1>=33 and marks2>=33 and marks3>=33 and avg>=40:
    print('pass')
else:
    print('fail')