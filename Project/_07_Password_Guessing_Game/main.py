"""
password guessing game:
3 levels - eay, medium, hard

computer selects a password from a list of words
user guesses the password
he gets a reply whether it is correct or how may words are correct and at the correct position

"""
import random

easy_words = [
    "cat", "dog", "sun", "sky", "red",
    "box", "car", "bat", "fox", "cup",
    "bee", "egg", "bus", "ant", "hat",
    "map", "pen", "key", "bed", "toy",
    "zip", "jam", "nut", "cow", "log",
    "fan", "web", "mud", "pig", "run",
    "top"
]

medium_words = [
    "apple", "river", "stone", "magic", "tiger",
    "planet", "forest", "silver", "shadow", "friend",
    "cloud", "dream", "flame", "bridge", "light",
    "hunter", "castle", "dragon", "winter", "garden",
    "puzzle", "rocket", "vision", "spirit", "legend",
    "silent", "travel", "harbor", "circle", "memory",
    "anchor", "throne", "galaxy", "signal", "candle"
]

hard_words = [
    "avalanche", "mystical", "labyrinth", "treasure",
    "confidence", "harmonica", "millennia", "spectral",
    "fractured", "evergreen", "horizon", "radiance",
    "chronicle", "vanguard", "paradox", "migration",
    "amethyst", "nightmare", "whispered", "insight",
    "marathon", "overgrown", "enchanted", "turbulent",
    "guardian", "existence", "precision", "triangle",
    "celestial", "hurricane", "originator", "migration"
]

def game(level):
    if level == 'easy':
        password = random.choice(easy_words)
    elif level == 'medium':
        password = random.choice(medium_words)
    elif level == 'hard':
        password = random.choice(hard_words)

    guess = input('Guess the password: ')
    guess_count = 1

    while guess.lower() != password.lower():
        guess_count += 1
        match_count = 0
        if len(password) != len(guess):
            print('Length not matched')
            guess = input('Guess the password: ')
            continue
        for i in range(len(password)):
            if guess[i].lower() == password[i].lower():
                match_count += 1
        print(f'{match_count} letters are correct and are at correct position.')
        guess = input('Guess the password: ')
    print(f'You took {guess_count} attempts to guess the password.')
    return

    # elif level == 'medium':
    #     password = random.choice(medium_words)
    #     guess = input('Guess the password: ')
    #     guess_count = 1
    #     while guess.lower() != password.lower():
    #         guess_count += 1
    #         match_count = 0
    #         if len(password) != len(guess):
    #             print('Length not matched')
    #             guess = input('Guess the password: ')
    #             continue
    #         for i in range(len(password)):
    #             if guess[i].lower() == password[i].lower():
    #                 match_count += 1
    #         print(f'{match_count} letters are correct and are at correct position.')
    #         guess = input('Guess the password: ')
    #     print(f'You took {guess_count} attempts to guess the password.')
    #     return
    #
    # elif level == 'hard':
    #     password = random.choice(hard_words)
    #     guess = input('Guess the password: ')
    #     guess_count = 1
    #     while guess.lower() != password.lower():
    #         guess_count += 1
    #         match_count = 0
    #         if len(password) != len(guess):
    #             print('Length not matched')
    #             guess = input('Guess the password: ')
    #             continue
    #         for i in range(len(password)):
    #             if guess[i].lower() == password[i].lower():
    #                 match_count += 1
    #         print(f'{match_count} letters are correct and are at correct position.')
    #         guess = input('Guess the password: ')
    #     print(f'You took {guess_count} attempts to guess the password.')
    #     return


print('Welcome to Password Guessing Game!')
print('3 levels - easy, medium, hard')
level = input('Choose a level: ')
game(level)