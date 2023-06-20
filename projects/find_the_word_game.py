import random

words = ['laptop', 'computer', 'mouse',
         'monitor', 'keyboard', 'microphone',
         'scanner', 'printer', 'projector',
         'joystick', 'pendrive', 'flashdrive',
         'speaker', 'webcam']
word = random.choice(words)

print("clue is PC")

turns = 12

length = len(word)

guesses = ''

while turns>0:

    wrong = 0
    for char in word:
        if char in guesses:
            print(char, end = ' ')

        else:
            print('-')
            wrong += 1

    if wrong == 0:
        print('you win. The word is',word)
        break
        
    guess = input('Enter the character: ')

    if guess in word:
        guesses = guesses + guess

    else:
        turns-=1
        print('wrong')
        print('you have', turns, 'more guesses')

    if turns == 0:
        print('You Loose. The word is', word)
