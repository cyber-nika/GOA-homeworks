def manual_len(my_list):
    length = 0
    index = 0  # starts with index 0
    while index < len(my_list):  # before index is less then the list
        length += 1  # each time add 1
        index += 1  # going to next index 
    print(length)

# იგივე ტესტები:
manual_len([1, 2, 3, 4, 5])
manual_len(["apple", "banana", "cherry"])
manual_len([True, False, True])
manual_len([10, 20, 30, 40, 50, 60])
manual_len([])
