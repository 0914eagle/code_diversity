
def any_int(x: float, y: float, z: float) -> bool:
    
    # Check if all numbers are integers
    if all(isinstance(num, int) for num in [x, y, z]):
        return x == y + z or y == x + z or z == x + y
    else:
        return False
