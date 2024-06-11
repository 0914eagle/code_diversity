def greatest_common_divisor(a: int, b: int) -> int:
    
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b


if __name__ ==