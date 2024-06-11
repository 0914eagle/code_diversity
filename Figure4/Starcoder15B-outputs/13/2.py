def greatest_common_divisor(a: int, b: int) -> int:
    
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        return greatest_common_divisor(a % b, b)
    else:
        return greatest_common_divisor(a, b % a)


