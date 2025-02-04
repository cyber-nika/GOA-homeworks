def repeat_string(n: int, s: str) -> str:
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    return s * n

print(repeat_string(3, "hello"))