
import math

def get_min_rod_length(triangles):
    # Calculate the maximum height of the triangles
    max_height = max([triangle[2] for triangle in triangles])

    # Calculate the minimum length of the rod required to support the triangles
    min_rod_length = 0
    for triangle in triangles:
        # Calculate the distance from the corner of the triangle to the center of the rod
        distance_from_corner = triangle[0] / 2 + triangle[1] / 2

        # Calculate the angle between the string and the rod
        angle = math.acos((triangle[0] ** 2 + triangle[1] ** 2 - triangle[2] ** 2) / (2 * triangle[0] * triangle[1]))

        # Calculate the minimum length of the string required to support the triangle
        min_string_length = distance_from_corner + max_height * math.sin(angle)

        # Update the minimum rod length
        min_rod_length = max(min_rod_length, min_string_length)

    return min_rod_length

triangles = []
for _ in range(int(input())):
    triangles.append(list(map(int, input().split())))

print(get_min_rod_length(triangles))

