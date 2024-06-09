
def is_solvable(a, b, c):
    # Calculate the area of the triangle
    area = abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2
    
    # Check if the area is zero
    if area == 0:
        return "No"
    
    # Calculate the center of the circle
    xc = (a[0] + b[0] + c[0]) / 3
    yc = (a[1] + b[1] + c[1]) / 3
    
    # Calculate the radius of the circle
    r = (area / abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))) ** 0.5
    
    # Check if the center is on the circle
    if (xc - r) ** 2 + yc ** 2 > r ** 2:
        return "No"
    
    # Calculate the angle of rotation
    angle = (b[1] - a[1]) * (c[0] - a[0]) - (b[0] - a[0]) * (c[1] - a[1])
    angle = angle / (2 * area)
    
    # Check if the angle is acute
    if angle < 0:
        return "No"
    
    return "Yes"

