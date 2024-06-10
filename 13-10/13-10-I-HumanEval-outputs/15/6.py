
def any_int(x: float, y: float, z: float) -> bool:
    
    
    return (x == y+z or x == z+y or y == x+z or y == z+x or z == x+y or z == y+x) and x.is_integer() and y.is_integer() and z.is_integer()

