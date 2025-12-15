# check for python in log.txt

with open('log.txt') as f:
    content = f.read()

if 'python' in content:
    print('python is present')

else:
    print('python is not present')