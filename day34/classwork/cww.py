def remove_one_element(lst, index):
    if 0 <= index < len(lst):
        lst.pop(index)
    print(lst)

remove_one_element([10, 20, 30, 40, 50], 2)
