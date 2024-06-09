
import math

def get_angle(x1, y1, x2, y2):
    # Calculate the dot product of the two vectors
    dot_product = x1 * x2 + y1 * y2
    
    # Calculate the magnitude of the two vectors
    magnitude_1 = math.sqrt(x1 ** 2 + y1 ** 2)
    magnitude_2 = math.sqrt(x2 ** 2 + y2 ** 2)
    
    # Calculate the cosine of the angle
    cosine_angle = dot_product / (magnitude_1 * magnitude_2)
    
    # Calculate the angle in radians
    angle = math.acos(cosine_angle)
    
    # Convert the angle to degrees
    angle = math.degrees(angle)
    
    return angle

n = int(input())
points = []

for i in range(n):
    x, y = map(float, input().split())
    points.append((x, y))

# Calculate the angle between the first two points and the last two points
angle_1 = get_angle(points[0][0], points[0][1], points[1][0], points[1][1])
angle_2 = get_angle(points[-1][0], points[-1][1], points[-2][0], points[-2][1])

# Calculate the average angle
angle = (angle_1 + angle_2) / 2

print(angle)

