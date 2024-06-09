
import math

def get_angle(x1, y1, x2, y2):
    # Calculate the difference in the x and y coordinates
    diff_x = x2 - x1
    diff_y = y2 - y1
    
    # Calculate the angle using the arctangent function
    angle = math.atan2(diff_y, diff_x)
    
    # Return the angle in degrees
    return math.degrees(angle)

# Test the function with the sample inputs
points = [[-2.14, 2.06], [-1.14, 2.04], [-2.16, 1.46], [-2.14, 0.70], [-1.42, 0.40], [-0.94, -0.48], [-1.42, -1.28], [-2.16, -1.62]]
print(get_angle(points[0], points[1]))

points = [[2.26, 1.44], [2.28, 0.64], [2.30, -0.30], [1.58, 0.66], [3.24, 0.66]]
print(get_angle(points[0], points[1]))

points = [[6.98, 2.06], [6.40, 1.12], [5.98, 0.24], [5.54, -0.60], [7.16, 0.30], [7.82, 1.24], [8.34, 0.24], [8.74, -0.76]]
print(get_angle(points[0], points[1]))

points = [[10.44, 2.06], [10.90, 0.80], [11.48, -0.48], [12.06, 0.76], [12.54, 2.06]]
print(get_angle(points[0], points[1]))

points = [[16.94, 2.42], [15.72, 2.38], [14.82, 1.58], [14.88, 0.50], [15.76, -0.16], [16.86, -0.20], [17.00, 0.88], [16.40, 0.92]]
print(get_angle(points[0], points[1]))

points = [[20.62, 3.00], [21.06, 2.28], [21.56, 1.36], [21.66, 0.56], [21.64, -0.52], [22.14, 2.32], [22.62, 3.04]]
print(get_angle(points[0], points[1]))

