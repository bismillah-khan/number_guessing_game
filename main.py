# number_guessing_game
# number_guessing_game.py

import random

def main():
    target = random.randint(1, 100)
    attempts = 0

    print("Guess the number between 1 and 100!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < target:
                print("Too Low!")
            elif guess > target:
                print("Too High!")
            else:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
