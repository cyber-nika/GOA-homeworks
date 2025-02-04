def generate_big_sentence(name, surname, age):
    sentence = f"ჩემი სახელია {name} {surname}, მე ვარ {age} წლის."
    print(sentence)

# მომხმარებლისგან ინფორმაციის მიღება
name = input("შეიყვანეთ თქვენი სახელი: ")
surname = input("შეიყვანეთ თქვენი გვარი: ")
age = input("შეიყვანეთ თქვენი ასაკი: ")

# ფუნქციის გამოძახება
generate_big_sentence(name, surname, age)

def my_split(main_string, string_to_split):
    result = main_string.split(string_to_split)
    print(result)

# მომხმარებლისგან ინფორმაციის მიღება
main_string = input("შეიყვანეთ მთავარი ტექსტი: ")
string_to_split = input("შეიყვანეთ დასაყოფი ტექსტი: ")

# ფუნქციის გამოძახება
my_split(main_string, string_to_split)