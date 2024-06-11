def greatest_common_divisor(a: int, b: int) -> int:
    
    if a == 0 or b == 0:
        return max(a, b)
    elif a == b:
        return a
    elif a > b:
        return greatest_common_divisor(a - b, b)
    else:
        return greatest_common_divisor(a, b - a)

