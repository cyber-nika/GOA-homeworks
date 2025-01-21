def manual_find(main_string, str_to_find):
    if not str_to_find:
        return -1
    for i in range(len(main_string) - len(str_to_find) + 1):
        if main_string[i:i + len(str_to_find)] == str_to_find:
            return i
    return -1

# Example usage
main_string = "Hello, this is a test."
str_to_find = "test"
print(manual_find(main_string, str_to_find))  # 17

str_to_find = "does not exist"
print(manual_find(main_string, str_to_find))  # -1
