
def change_base(x: int, base: int) -> str:
    
    if base < 2 or base > 10:
        raise ValueError("base must be between 2 and 10")
    digits = "0123456789ABCDEF"
    if x == 0:
        return "0"
    result = ""
    while x > 0:
        result = digits[x % base] + result
        x //= base
    return result

