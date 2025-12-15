# copy of text.txt

with open('text.txt') as f:
    content = f.read()

with open('text_copy.txt', 'w') as f:
    f.write(content)

with open('text_copy.txt') as f:
    print(f.read())