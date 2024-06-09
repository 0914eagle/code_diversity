
def check_solution(a, b, c):
    # Calculate the center of the circle passing through the three points
    xc = (a[0] + b[0] + c[0]) / 3
    yc = (a[1] + b[1] + c[1]) / 3
    
    # Calculate the radius of the circle
    r = ((a[0] - xc) ** 2 + (a[1] - yc) ** 2) ** 0.5
    
    # Calculate the angle between the line connecting the center and point a, and the x-axis
    angle = (b[1] - yc) / (b[0] - xc)
    
    # Calculate the coordinates of point b after rotation
    xb = xc + r * math.cos(angle)
    yb = yc + r * math.sin(angle)
    
    # Check if the coordinates of point b after rotation are the same as the coordinates of point c
    if xb == c[0] and yb == c[1]:
        return "Yes"
    else:
        return "No"

