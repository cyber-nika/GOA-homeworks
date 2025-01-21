user_input = int(input("შეიყვანეთ მთელი რიცხვი: "))
total_sum = 0
for num in range(user_input + 1):
    total_sum += num
print(f"დიაპაზონის ყველა რიცხვის ჯამი: {total_sum}")
