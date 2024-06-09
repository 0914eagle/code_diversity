
def get_required_length(triangles):
    
    # Calculate the sum of the areas of all the triangles
    area_sum = sum([triangle[0] * triangle[1] for triangle in triangles])

    # Calculate the maximum length of the rod needed to support the triangles
    max_length = (area_sum / 2.0) ** 0.5

    return max_length

