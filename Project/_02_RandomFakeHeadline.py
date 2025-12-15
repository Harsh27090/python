# lists - subject, action, place
# random.choice() - to randomly choose from a list
# string concatenation - to concatenate selected strings
# input() - to ask if user want to generate another headline
# while - to continue until user says no
import random

subjects = ['Sharukh Khan', 'MS Dhoni', 'Virat Kohli', 'Rohit Sharma', 'Narendra Modi','AB Deviliers']
actions = ['spotted riding a buffalo', 'was being chased by a dog', 'spotted dancing']
places = ['in the train', 'near Taj Mahal', 'on the road', 'in aeroplane', 'on top of a building']

# inp = input('Do you want to generate a fake headline? (y/n)')
# subject = random.choice(subjects)
# action = random.choice(actions)
# place = random.choice(places)
# print(subject+' '+action+' '+place)

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)
    print(subject+' '+action+' '+place)
    inp = input('Do you want to generate another? (y/n)')
    if inp.strip().lower() == 'n':
        print('Thank you!') 
        break
