
import math

def get_angle(x1, y1, x2, y2):
    # Calculate the dot product of the two vectors
    dot_product = x1 * x2 + y1 * y2

    # Calculate the magnitude of the two vectors
    magnitude_1 = math.sqrt(x1 ** 2 + y1 ** 2)
    magnitude_2 = math.sqrt(x2 ** 2 + y2 ** 2)

    # Calculate the cosine of the angle between the vectors
    cosine_angle = dot_product / (magnitude_1 * magnitude_2)

    # Calculate the angle in radians
    angle = math.acos(cosine_angle)

    # Convert the angle to degrees
    angle = math.degrees(angle)

    return angle

def solve(points):
    # Initialize the angle to 0
    angle = 0

    # Iterate through the points
    for i in range(len(points)):
        # Calculate the angle between the current point and the previous point
        angle += get_angle(points[i][0], points[i][1], points[i-1][0], points[i-1][1])

    # Return the total angle
    return angle

points = []

# Read the number of points
n = int(input())

# Read the points
for i in range(n):
    x, y = map(float, input().split())
    points.append([x, y])

# Solve the problem
angle = solve(points)

# Print the result
print(angle)

