def change_base(x: int, base: int):
    
    if base < 10:
        return str(x)
    else:
        return str(x)[::-1].zfill(base)


