correct_password = "mypassword"
attempt_count = 0
while True:
    user_password = input("შეიყვანეთ პაროლი: ")
    attempt_count += 1
    if user_password == correct_password:
        print(f"Access granted. ცდების რაოდენობა: {attempt_count}")
        break
