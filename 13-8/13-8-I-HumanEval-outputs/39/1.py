
def change_base(x: int, base: int) -> str:
    
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9")
    if x < 0:
        raise ValueError("x must be non-negative")

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    quotient = x
    remainder = 0
    converted_string = ""

    while quotient > 0:
        remainder = quotient % base
        converted_string = digits[remainder] + converted_string
        quotient = quotient // base

    if converted_string == "":
        converted_string = "0"

    return converted_string

