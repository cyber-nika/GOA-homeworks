my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Error: Tried to access an index that doesn't exist in the list.")