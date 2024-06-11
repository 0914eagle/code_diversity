def change_base(x: int, base: int):
    
    if x == 0:
        return "0"
    if base == 10:
        return str(x)
    if x < 0:
        return "-" + change_base(-x, base)
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = ""
    while x > 0:
        s = digits[x % base] + s
        x //= base
    return s


if __name__ == "__main__":
    import doctest
