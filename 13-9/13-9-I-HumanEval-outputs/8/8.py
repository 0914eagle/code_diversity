
def right_angle_triangle(a: int, b: int, c: int) -> bool:
    
    return (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (c**2 + a**2 == b**2)

