
def change_base(x: int, base: int) -> str:
    
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9")
    if x == 0:
        return "0"
    if x < 0:
        sign = "-"
        x *= -1
    else:
        sign = ""
    result = ""
    while x > 0:
        result = str(x % base) + result
        x //= base
    return sign + result

