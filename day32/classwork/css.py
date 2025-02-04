def generate_big_sentence(name, surname, age):
    sentence = f"ჩემი სახელია {name} {surname}, მე ვარ {age} წლის."
    print(sentence)

# მომხმარებლისგან ინფორმაციის მიღება
name = input("შეიყვანეთ თქვენი სახელი: ")
surname = input("შეიყვანეთ თქვენი გვარი: ")
age = input("შეიყვანეთ თქვენი ასაკი: ")

# ფუნქციის გამოძახება
generate_big_sentence(name, surname, age)
