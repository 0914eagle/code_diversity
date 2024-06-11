def largest_divisor(n: int) -> int:
    
    if n % 2 == 0:
        return n // 2
    else:
        return n - 1


