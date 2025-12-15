# a file is identical and matches another

with open('text_copy.txt') as f:
    content1 = f.read()

with open('text.txt') as f:
    content2 = f.read()

if content1==content2:
    print('identical')

else:
    print('different')