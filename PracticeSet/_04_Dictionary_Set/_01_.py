# dictionary of hindi words with english translation

my_dict = {
    'Safarjan': 'Apple',
    'Kela': 'Banana',
    'Billi': 'Cat',
    'Kutta': 'Dog',
    'Machhli': 'Fish'
}

trans= input('Enter a word:')
print(my_dict.get(trans, 'Not found!'))