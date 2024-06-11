def largest_divisor(n: int) -> int:
    
    divisor = int(n / 2)
    while divisor > 0:
        if n % divisor == 0:
            return divisor
        divisor -= 1
    return 1


if