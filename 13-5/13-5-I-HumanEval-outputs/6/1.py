
def any_int(x: float, y: float, z: float) -> bool:
    
    return (x == int(x) and y == int(y) and z == int(z) and (x + y == z or x + z == y or y + z == x))

