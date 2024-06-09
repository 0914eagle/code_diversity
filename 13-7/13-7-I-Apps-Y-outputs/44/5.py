
import math

def get_min_rod_length(triangles):
    
    # Calculate the maximum height of the triangles
    max_height = max([triangle[2] for triangle in triangles])

    # Calculate the minimum distance between the centers of the triangles
    min_distance = 2 * max_height * (1 + math.sin(math.pi / 3))

    # Return the sum of the minimum distance and the maximum height
    return min_distance + max_height

triangles = [[3, 3, 3], [4, 4, 5]]
print(get_min_rod_length(triangles))

