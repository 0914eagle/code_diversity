
def get_min_rod_length(triangles):
    
    # Calculate the maximum height of the triangles
    max_height = max([triangle[0] for triangle in triangles])

    # Calculate the minimum length of the rod required to hang the triangles
    min_rod_length = 0
    for triangle in triangles:
        min_rod_length += triangle[0] + triangle[1] * 2

    # Add the height of the triangles to the minimum length of the rod
    min_rod_length += max_height

    return min_rod_length

