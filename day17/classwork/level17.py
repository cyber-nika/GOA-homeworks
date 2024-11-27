# პაროლის მართვა
correct_password = "my_secret_password"  # აქ შეინახეთ თქვენი პაროლი

# პაროლის შესამოწმებლად ცვლადები
counter = 0  # განსაზღვრავს, რამდენჯერ შეიტანეს პაროლი

# while ციკლი პაროლის შესამოწმებლად
while True:
    user_password = input("შეიყვანეთ პაროლი: ")
    counter += 1  # აღინიშნება, რომ პაროლი შეიყვანა
    if user_password == correct_password:
        print("Access granted!")
        print(f"პაროლი {counter} ჯერ იქნა შეყვანილი.")
        break  # ციკლი დაიხურება, რადგან პაროლი სწორი იყო
    else:
        print("პაროლი არასწორია, სცადეთ ისევ.")