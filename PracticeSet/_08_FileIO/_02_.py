import random

def game():
    print('You are playing game:')
    score = random.randint(0,100)
    print('Your score is:',score)

    with open('hi-score.txt') as f:
        hi_score = f.read()
        if hi_score != '':
            hi_score = int(hi_score)
        else:
            hi_score = 0

    if score > int(hi_score):
        with open('hi-score.txt', 'w') as f:
            f.write(str(score))
    return score

open("hi-score.txt", "w").close() # clearing the file before use
for i in range(10):
    print(game())

with open('hi-score.txt') as f:
    content = f.read()
    print(f'hi-score:{content}')






