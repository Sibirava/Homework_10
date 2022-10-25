import random


def try_guess_number(number, guess):
    tries = 0
    msg = f"Empty tries"

    for t in range(1, 5):
        tries += 1
        if guess > number:
            guess = int(input("Number is lower than guess.One more try:"))
        elif guess < number:
            guess = int(input("Number is bigger than guess.One more try:"))
        else:
            msg = f"You win. You guessed the number in {tries} tries"
            break
    return msg



def main():
    number = random.randint(1, 101)
    print(number)

    print("Hi! Let's play! Guess number from 1 to 100")

    guess = int(input("Your guess: "))

    game = try_guess_number(number, guess)

    print(game)


main()
