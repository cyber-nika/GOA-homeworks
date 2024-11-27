# მომხმარებლის რიცხვების მიღება
num1 = float(input("შეიტანეთ პირველი რიცხვი: "))
num2 = float(input("შეიტანეთ მეორე რიცხვი: "))

# ოპერაციების გამოთვლა
sum_result = num1 + num2            # ჯამი
difference = num1 - num2            # სხვაობა
product = num1 * num2               # ნამრავლი
quotient = num1 / num2              # განაყოფი
first_div_second = num1 / num2      # პირველი რიცხვის წილი მეორეზე
second_div_first = num2 / num1      # მეორე რიცხვის წილი პირველზე

# შედეგების დაბეჭდვა
print(f"ჯამი: {sum_result}")
print(f"სხვაობა: {difference}")
print(f"ნამრავლი: {product}")
print(f"განაყოფი: {quotient}")
print(f"პირველი რიცხვის წილი მეორეზე: {first_div_second}")
print(f"მეორე რიცხვის წილი პირველზე: {second_div_first}")
