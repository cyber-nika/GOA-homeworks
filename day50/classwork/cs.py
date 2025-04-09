# 1) TypeError-ის გამოწვევა და დამუშავება
try:
    num = 10  # ცვლადი, სადაც ინახება მთელი რიცხვი
    result = num + "20"  # განზრახ შეცდომა (int + str)
except TypeError as e:
    print(f"TypeError მოხდა: {e}")

# 2) მომხმარებლის შეყვანის კონტროლი ყველა შესაძლო შეცდომისთვის
try:
    user_input = input("შეიყვანეთ სახელი: ")
    if not user_input.isalpha():
        raise ValueError("სახელი უნდა შეიცავდეს მხოლოდ ასოებს")
    print(f"თქვენი შეყვანილი სახელი: {user_input}")
except ValueError as ve:
    print(f"მონაცემთა შეცდომა: {ve}")
except KeyboardInterrupt:
    print("პროცესი შეჩერდა მომხმარებლის მიერ.")
except Exception as e:
    print(f"უცნობი შეცდომა მოხდა: {e}")
