# censor list of words

words = ['donkey', 'monkey', 'dying', 'terror', 'murder']
# content = ''

with open('uncensored.txt') as f:
    content = f.read()

for word in words:
    content = content.replace(word, '#'*len(word))

with open('uncensored.txt', 'w') as f:
    f.write(content)

with open('uncensored.txt') as f:
    print(f.read())
