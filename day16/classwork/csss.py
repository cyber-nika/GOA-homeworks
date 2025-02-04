import random

# Set a random number between 1 and 10
my_num = random.randint(1, 10)

# Initialize counter
attempts = 0

while True:
    # Get user input
    user_guess = int(input("Guess the number (1-10): "))
    attempts += 1

    # Check if the guess is correct
    if user_guess == my_num:
        print("You guessed it!")
        print("Attempts:", attempts)
        break
    else:
        print("Wrong guess, try again.")
