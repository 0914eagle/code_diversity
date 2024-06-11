def change_base(x: int, base: int):
    
    if x == 0:
        return "0"
    if x < 0:
        return "-" + change_base(-x, base)
    result = ""
    while x > 0:
        x, r = divmod(x, base)
        result = str(r) + result
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()