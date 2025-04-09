# 2. List Index Access
def access_list_element():
    sample_list = [1, 2, 3, 4, 5]
    try:
        index = int(input("Enter an index to access in the list [1, 2, 3, 4, 5]: "))
        print(f"Element at index {index} is {sample_list[index]}")
    except IndexError:
        print("Error: Index out of range.")
    except ValueError:
        print("Error: Please enter a valid integer.")