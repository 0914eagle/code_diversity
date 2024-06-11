def greatest_common_divisor(a: int, b: int) -> int:
    
    return a if b == 0 else greatest_common_divisor(b, a % b)


