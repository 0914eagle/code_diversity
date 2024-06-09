
def is_solvable(a, b, c):
    # Calculate the area of the triangle
    area = triangle_area(a, b, c)
    
    # Check if the area is zero
    if area == 0:
        return "No"
    
    # Calculate the centroid of the triangle
    centroid = triangle_centroid(a, b, c)
    
    # Calculate the angle between the sides of the triangle
    angle = triangle_angle(a, b, c)
    
    # Check if the angle is acute
    if angle < 90:
        return "Yes"
    else:
        return "No"

def triangle_area(a, b, c):
    return 0.5 * abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))

def triangle_centroid(a, b, c):
    return [(a[0] + b[0] + c[0]) / 3, (a[1] + b[1] + c[1]) / 3]

def triangle_angle(a, b, c):
    return math.degrees(math.acos(((b[0] - a[0]) * (c[0] - a[0]) + (b[1] - a[1]) * (c[1] - a[1])) / ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)))

