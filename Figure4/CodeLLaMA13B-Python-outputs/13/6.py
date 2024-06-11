def greatest_common_divisor(a: int, b: int) -> int:
    
    if a == 0 or b == 0:
        return max(a, b)
    if a == b:
        return a
    if a > b:
        return greatest_common_divisor(a - b, b)
    return greatest_common_divisor(a, b - a)


