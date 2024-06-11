def greatest_common_divisor(a: int, b: int) -> int:
    
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return greatest_common_divisor(a % b, b)
    return greatest_common_divisor(a, b % a)


