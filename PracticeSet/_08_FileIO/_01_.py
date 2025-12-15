# twinkle in poem.txt or not

with open('poem.txt') as f:
    content = f.read()
    if 'twinkle' in content:
        print('present')
    else:
        print('not present')