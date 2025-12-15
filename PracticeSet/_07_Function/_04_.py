# recursive function for sum of first n natural nos.

def sumnatural(num):
    if num==1:
        return 1

    return num + sumnatural(num-1)

print(sumnatural(5))

