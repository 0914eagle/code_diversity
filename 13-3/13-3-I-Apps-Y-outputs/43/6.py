
import math

def get_min_rod_length(triangles):
    # Calculate the maximum height of the triangles
    max_height = max([triangle[2] for triangle in triangles])

    # Calculate the minimum length of the rod required to hang the triangles
    min_rod_length = 0
    for triangle in triangles:
        rod_length = triangle[0] + triangle[1] + max_height
        if rod_length > min_rod_length:
            min_rod_length = rod_length

    return min_rod_length

triangles = []
for _ in range(int(input())):
    triangles.append(list(map(int, input().split())))

print(get_min_rod_length(triangles))

