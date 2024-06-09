
def get_min_rod_length(triangles):
    
    # Calculate the maximum height of the triangles
    max_height = max([triangle[0] for triangle in triangles])

    # Calculate the maximum distance from the center of the rod to the base of the triangles
    max_distance = max([(triangle[1] ** 2 + triangle[2] ** 2) ** 0.5 for triangle in triangles])

    # Calculate the minimum required length for the rod
    min_rod_length = max_height + max_distance

    return min_rod_length

