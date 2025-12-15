letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

a = input("Enter your name:")
print(letter.replace('<|Name|>', a).replace('<|Date|>', '26 November, 2025'))

