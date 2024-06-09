
import math

def get_min_rod_length(triangles):
    # Calculate the minimum rod length by finding the maximum height of the triangles
    max_height = 0
    for triangle in triangles:
        height = triangle[0] * math.sin(math.radians(60))
        if height > max_height:
            max_height = height
    return max_height * 2

triangles = []
for _ in range(int(input())):
    triangles.append(list(map(int, input().split())))

print(f"{get_min_rod_length(triangles):.4f}")

