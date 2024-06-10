
def change_base(x: int, base: int) -> str:
    
    if base < 2 or base > 9:
        raise ValueError("Invalid base")
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if x == 0:
        return "0"
    result = ""
    while x > 0:
        result = digits[x % base] + result
        x //= base
    return result

