
def any_int(x: float, y: float, z: float) -> bool:
    
    return (x == y+z) and (x.is_integer()) and (y.is_integer()) and (z.is_integer())
