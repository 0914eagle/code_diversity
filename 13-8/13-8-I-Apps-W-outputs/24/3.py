
def is_solvable(a, b, c):
    # Calculate the area of the triangle
    area = triangle_area(a, b, c)
    
    # Check if the triangle is isosceles
    if is_isosceles(a, b, c):
        return "Yes"
    
    # Check if the triangle is equilateral
    if is_equilateral(a, b, c):
        return "Yes"
    
    # Check if the triangle has a right angle
    if has_right_angle(a, b, c):
        return "Yes"
    
    # If none of the above conditions are met, then the problem has no solution
    return "No"

def triangle_area(a, b, c):
    # Calculate the area of the triangle
    return 0.5 * abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))

def is_isosceles(a, b, c):
    # Check if two sides of the triangle are equal
    return a[0] == b[0] or a[1] == b[1] or c[0] == b[0] or c[1] == b[1]

def is_equilateral(a, b, c):
    # Check if all sides of the triangle are equal
    return a[0] == b[0] and a[1] == b[1] and c[0] == b[0] and c[1] == b[1]

def has_right_angle(a, b, c):
    # Check if one of the vertices is the origin and the other two vertices form a right angle
    return a[0] == 0 and a[1] == 0 and (b[0] == 0 or b[1] == 0) and (c[0] == 0 or c[1] == 0)

