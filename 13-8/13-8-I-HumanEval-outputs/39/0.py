
def change_base(x: int, base: int) -> str:
    
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9")
    if x < 0:
        raise ValueError("Input number must be non-negative")
    if x == 0:
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    converted = ""
    while x > 0:
        converted = digits[x % base] + converted
        x //= base
    return converted

