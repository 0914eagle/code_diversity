def greatest_common_divisor(a: int, b: int) -> int:
    
    if a == 0:
        return b
    return greatest_common_divisor(b % a, a)


