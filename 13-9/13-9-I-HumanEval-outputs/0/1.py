
def change_base(x: int, base: int) -> str:
    
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9")
    if x < 0:
        raise ValueError("Input number must be non-negative")

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base_digits = digits[:base]

    if x == 0:
        return "0"

    result = ""
    while x > 0:
        result = base_digits[x % base] + result
        x //= base

    return result

