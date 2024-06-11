def greatest_common_divisor(a: int, b: int) -> int:
    
    if a == 0 or b == 0:
        return max(a, b)
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if a < b:
        a, b = b, a
    return greatest_common_divisor(b % a, a)


