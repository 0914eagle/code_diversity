def change_base(x: int, base: int):
    
    if x == 0:
        return "0"
    if x < 0:
        return "-" + change_base(-x, base)
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base
    return "".join(digits[::-1])


if __name__ == "__main__":
    import do