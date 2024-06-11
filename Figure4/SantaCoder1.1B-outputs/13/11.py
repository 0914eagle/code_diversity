def greatest_common_divisor(a: int, b: int) -> int:
    
    while a % b != 0:
        a, b = b, a % b
    return b


