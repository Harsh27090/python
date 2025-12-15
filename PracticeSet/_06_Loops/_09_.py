num = int(input('Enter a number: '))

for i in range(1,num+1):
    if i==1 or i==num:
        print('*'* num)
    else:
        print('*'*1+' '*(num-2)+'*'*1)