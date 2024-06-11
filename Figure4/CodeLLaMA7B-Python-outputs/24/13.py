def largest_divisor(n: int) -> int:
    
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i


if