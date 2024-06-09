
def right_angle_triangle(a: int, b: int, c: int) -> bool:
    
    sides = [a, b, c]
    sides.sort()
    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
