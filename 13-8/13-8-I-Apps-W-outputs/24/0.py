
def is_solvable(a, b, c):
    # Calculate the area of the triangle using the cross product of the sides
    area = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    
    # Check if the area is zero
    if area == 0:
        return "No"
    
    # Calculate the center of the circle passing through the three points
    center = [(a[0] + b[0] + c[0]) / 3, (a[1] + b[1] + c[1]) / 3]
    
    # Calculate the radius of the circle
    radius = (center[0] - a[0]) ** 2 + (center[1] - a[1]) ** 2
    
    # Calculate the angle of rotation
    angle = (180 / 3.14159) * math.acos((b[0] - a[0]) * (c[0] - a[0]) + (b[1] - a[1]) * (c[1] - a[1]))
    
    # Check if the angle is acute
    if angle < 90:
        return "Yes"
    else:
        return "No"

