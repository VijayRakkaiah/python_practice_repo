import random

number = random.randint(1,100)

while True:
    guess = int(input('Find the number between 1 to 100: '))

    if guess == number:
        print("Correct. You find the number")
        break

    elif guess > number:
        print("you're  guess is too high")

    else:
        print("you're guess is too small")
        
