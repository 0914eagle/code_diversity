
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

n = int(input())
points = []

for i in range(n):
    x, y = map(float, input().split())
    points.append((x, y))

# Calculate the angle between each pair of points
angles = []
for i in range(n):
    for j in range(i+1, n):
        angle = get_angle(points[i][0], points[i][1], points[j][0], points[j][1])
        angles.append(angle)

# Print the minimum angle
print(min(angles))

