import random
my_num = random.randint(1, 10)
guess_count = 0
while True:
    user_guess = int(input("გამოიცანი რიცხვი 1-დან 10-მდე: "))
    guess_count += 1
    if user_guess == my_num:
        print(f"You guessed! ცდების რაოდენობა: {guess_count}")
        break
