def greatest_common_divisor(a: int, b: int) -> int:
    
    if a == 0 or b == 0:
        return max(a, b)
    if a < b:
        return greatest_common_divisor(b, a)
    return greatest_common_divisor(b, a % b)


