# 3. Dictionary Key Access
def access_dictionary_key():
    sample_dict = {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}
    try:
        key = input("Enter a key to access in the dictionary ('name', 'age', 'city'): ")
        print(f"The value for '{key}' is: {sample_dict[key]}")
    except KeyError:
        print(f"Error: '{key}' does not exist in the dictionary.")