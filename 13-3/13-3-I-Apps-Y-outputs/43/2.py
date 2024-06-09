
import math

def get_min_rod_length(triangles):
    # Calculate the maximum height of the triangles
    max_height = max([triangle[2] for triangle in triangles])

    # Calculate the minimum length of the rod required to support the triangles
    min_rod_length = 0
    for triangle in triangles:
        rod_length = triangle[0] + triangle[1] + triangle[2]
        if rod_length > min_rod_length:
            min_rod_length = rod_length

    # Add the maximum height of the triangles to the minimum length of the rod
    return min_rod_length + max_height

triangles = []
for _ in range(int(input())):
    triangles.append(list(map(int, input().split())))

print(get_min_rod_length(triangles))

