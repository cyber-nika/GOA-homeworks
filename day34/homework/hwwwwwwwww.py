def find_maximum(numbers: list) -> int:
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
