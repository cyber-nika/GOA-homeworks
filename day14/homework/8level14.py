# მომხმარებელს ვთხოვთ 3 რიცხვის შეყვანას
num1 = int(input("გთხოვთ, შეიტანოთ პირველი რიცხვი: "))  # პირველი რიცხვი
num2 = int(input("გთხოვთ, შეიტანოთ მეორე რიცხვი: "))  # მეორე რიცხვი
num3 = int(input("გთხოვთ, შეიტანოთ მესამე რიცხვი: "))  # მესამე რიცხვი

# შექმნათ დიაპაზონი range(num1, num2, num3)
for num in range(num1, num2, num3):
    print(num ** 2)  # დაბეჭდეთ ყოველ რიცხვის კვადრატი