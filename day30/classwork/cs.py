name = input("please, enter your name: ")

choice = input("choose (u - uppercase, l - lowercase): ")

if choice == "u":
    print("your name in Uppercase: ", name.upper())
elif choice == "l":
    print("your name in Lowercase: ", name.lower())
else:
    print("wrong information")
