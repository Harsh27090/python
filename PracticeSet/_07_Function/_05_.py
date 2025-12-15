def pattern1(num):
    for i in range(num,0,-1):
        print('*'*i)

def rec_pattern1(num):
    if num==0:
        return
    print('*'*num)
    rec_pattern1(num-1)

pattern1(3)
rec_pattern1(3)