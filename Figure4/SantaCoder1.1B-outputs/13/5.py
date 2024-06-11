def greatest_common_divisor(a: int, b: int) -> int:
    
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)


