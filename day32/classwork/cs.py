def generate_big_sentence(name, surname, age):
    sentence = "ჩემი სახელია {} {}, მე ვარ {} წლის.".format(name, surname, age)
    print(sentence)

# მომხმარებლისგან ინფორმაციის მიღება
name = input("შეიყვანეთ თქვენი სახელი: ")
surname = input("შეიყვანეთ თქვენი გვარი: ")
age = input("შეიყვანეთ თქვენი ასაკი: ")

# ფუნქციის გამოძახება
generate_big_sentence(name, surname, age)
