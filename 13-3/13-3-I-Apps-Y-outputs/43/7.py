
import math

def get_min_rod_length(triangles):
    # Calculate the maximum height of the triangles
    max_height = max([triangle[2] for triangle in triangles])

    # Calculate the minimum length of the rod required to hold the triangles
    min_rod_length = 0
    for triangle in triangles:
        rod_length = triangle[0] + triangle[1] + triangle[2]
        min_rod_length += rod_length

    # Add the height of the triangles to the minimum rod length
    min_rod_length += max_height

    return min_rod_length

triangles = []
for _ in range(int(input())):
    triangles.append(list(map(int, input().split())))

print(get_min_rod_length(triangles))

