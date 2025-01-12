def manual_range(start, end, step):
    # A loop that loops through a range and prints only even numbers
    for number in range(start, end, step):
        if number % 2 == 0:  # if number is even
            print(number)

# Query the function with different arguments

manual_range(1, 20, 2)   # first text from 1 to 20, step 2
manual_range(5, 50, 5)   # second text from 5 to 50, step 5
manual_range(10, 30, 3)  # third text from 10 to 30, step 3
manual_range(0, 15, 1)   # fourth text: from 0 to 15, step 1
manual_range(7, 100, 7)  # fifth text: from 7 to 100, step 7
