def greatest_common_divisor(a: int, b: int) -> int:
    
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)


