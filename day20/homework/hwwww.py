start = int(input("Enter the starting integer: "))
end = int(input("Enter the ending integer: "))

total_sum = 0
for num in range(start, end + 1):
    total_sum += num

print(f"The sum of numbers between {start} and {end} is: {total_sum}")
