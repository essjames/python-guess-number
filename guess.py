import random

player = input("What is your name? ")
amount_of_guesses = 0
answer = random.randint(0,15)

while amount_of_guesses <= 5:
    greeting = (f"Hi {player}! I am thinking of a number between 1-15...")
    guess = int(input("You have five chances to guess what I am thinking, pick a number between 1-15:  "))
    amount_of_guesses += 1
    if guess == answer:
        print(f"{player} you have won!!! You guessed {guess} & The Computer was thinking of {answer}")
        break
    elif guess != answer and amount_of_guesses == 5:
        print(f"Oops you have ran out of Guesses {player} :(! Better look next time! The Computer was thinking of {answer}")
        break
    elif guess != answer and amount_of_guesses < 5:
        print(f"Opps! Guess Again {name}!")
else:
    print(f"You did not guess correctly {player}, the number was {answer}")
