def largest_divisor(n: int) -> int:
    
    if n % 2 == 0:
        return n
    else:
        return largest_divisor(n // 2)


