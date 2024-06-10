
def any_int(x: float, y: float, z: float) -> bool:
    
    return ((x == int(x) and y == int(y) and z == int(z)) and (x + y == z or y + z == x or z + x == y))

