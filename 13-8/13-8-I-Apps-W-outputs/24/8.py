
def is_solvable(a, b, c):
    # Calculate the area of the triangle
    area = (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2
    
    # Check if the area is zero
    if area == 0:
        return "No"
    
    # Calculate the center of the circle
    xc = (a[0] + b[0] + c[0]) / 3
    yc = (a[1] + b[1] + c[1]) / 3
    
    # Calculate the radius of the circle
    radius = ((a[0] - xc) ** 2 + (a[1] - yc) ** 2) ** 0.5
    
    # Check if the center is on the line
    if xc == 0 and yc == 0:
        return "No"
    
    # Check if the circle passes through the point
    if (a[0] - xc) ** 2 + (a[1] - yc) ** 2 == radius ** 2:
        return "Yes"
    
    # Check if the circle is tangent to the line
    if (a[0] - xc) ** 2 + (a[1] - yc) ** 2 == radius ** 2 + 1:
        return "Yes"
    
    # Otherwise, the problem has no solution
    return "No"

