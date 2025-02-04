def sum_divisible_by_three(start: int, end: int) -> int:
    return sum(num for num in range(start, end + 1) if num % 3 == 0)
