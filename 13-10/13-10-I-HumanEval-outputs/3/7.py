
def change_base(x: int, base: int) -> str:
    
    if x == 0:
        return "0"
    digits = "0123456789ABCDEF"
    converted = ""
    while x > 0:
        converted = digits[x % base] + converted
        x //= base
    return converted

