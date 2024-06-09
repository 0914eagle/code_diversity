
import math

def get_angle(x1, y1, x2, y2):
    # Calculate the dot product of the two vectors
    dot_product = x1 * x2 + y1 * y2

    # Calculate the magnitude of the two vectors
    mag1 = math.sqrt(x1 ** 2 + y1 ** 2)
    mag2 = math.sqrt(x2 ** 2 + y2 ** 2)

    # Calculate the angle between the two vectors
    angle = math.acos(dot_product / (mag1 * mag2))

    return angle

def solve(points):
    # Initialize the angle to 0
    angle = 0

    # Iterate through the points and calculate the angle between each pair of points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            angle += get_angle(x1, y1, x2, y2)

    # Return the average angle
    return angle / len(points)

# Test the solve function
points = [
    (-2.14, 2.06),
    (-1.14, 2.04),
    (-2.16, 1.46),
    (-2.14, 0.70),
    (-1.42, 0.40),
    (-0.94, -0.48),
    (-1.42, -1.28),
    (-2.16, -1.62)
]
print(solve(points))

