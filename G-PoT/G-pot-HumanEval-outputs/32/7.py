
def any_int(x: float, y: float, z: float) -> bool:
    
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        return x == y + z or y == x + z or z == x + y
    else:
        return False
