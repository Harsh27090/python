# max of 3

def maxOfThree(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c

a = int(input())
b = int(input())
c = int(input())

maxi = maxOfThree(a,b,c)
print(maxi)