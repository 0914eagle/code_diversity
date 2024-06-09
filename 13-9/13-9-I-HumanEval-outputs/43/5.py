
def greatest_common_divisor(a: int, b: int) -> int:
    
    if a == 0 or b == 0:
        return 0
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

