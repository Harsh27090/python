# censor 'donkey' with '######'

word = 'donkey'

with open('donkey.txt') as f:
    content = f.read()

new_content = content.replace(word, '######')

with open('donkey.txt', 'w') as f:
    f.write(new_content)

with open('donkey.txt') as f:
    print(f.read())