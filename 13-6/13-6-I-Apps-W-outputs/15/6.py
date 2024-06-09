
def get_rectangular_isosceles_triangle(x, y):
    # Find the length of the hypotenuse of the right triangle
    hypotenuse = max(x, y)
    
    # Find the length of the other two sides of the triangle
    side1 = hypotenuse - x
    side2 = hypotenuse - y
    
    # Find the coordinates of the two points on the hypotenuse
    x1 = 0
    y1 = hypotenuse
    x2 = hypotenuse
    y2 = 0
    
    # Find the coordinates of the two points on the other sides of the triangle
    x3 = side1
    y3 = 0
    x4 = 0
    y4 = side2
    
    # Return the coordinates of the required points
    return x1, y1, x2, y2, x3, y3, x4, y4

