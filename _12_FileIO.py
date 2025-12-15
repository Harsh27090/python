# 1. read
st = 'Harsh is learning python for data science'

f = open('file.txt','r') # r is by default, no need to write 'r'
data = f.read()
print(data)
f.close() # its necessary to close the file after you have done working

# 2. write
f = open('myfile.txt', 'w')
f.write(st)
f.close()

# 3. readline() - reads lines one by one from thr current file pointer
# 4. readlines() - reads all remaining lines from the current file pointer and returns a list with each line as an element
# as a result, after using readlines() there won't be any remaining lines so readline() will return ''
f = open('file.txt')

# print(f.readlines())

# line1=f.readline()
# print(line1, type(line1))
# line2=f.readline()
# print(line2, type(line2))
# line3=f.readline()
# print(line3, type(line3))
# line4=f.readline()
# print(line4, type(line4))
# line5=f.readline()
# print(line5, type(line5))
# line6=f.readline()
# print(line6=='')

line = f.readline()
while line != '':
    print(line, end='')
    line = f.readline()

f.close()

# 5. append

f = open('myfile.txt', 'w+') # using 'w'/'w+', clears the old data and write new data
f.write('Johny Johny')
f.seek(0) # current pointer to the start of file
print(f.readlines())
f.close()

f = open('myfile.txt', 'a+')
f.write('\nYes papa')
f.seek(0)
print(f.readlines())
f.close()

# r+ -> read and write
# w+ -> write and read
# a+ -> append and write

# with -> the same can be written using with, you don't have to close the file
with open('myfile.txt') as f:
    line = f.readline()
    while line!='':
        print(line,end='')
        line = f.readline()






