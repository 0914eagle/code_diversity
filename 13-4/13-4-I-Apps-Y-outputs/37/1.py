
def get_min_rod_length(triangle_list):
    # Calculate the sum of the areas of all triangles
    total_area = sum([triangle[0] * triangle[1] for triangle in triangle_list])

    # Calculate the perimeter of the largest triangle
    max_perimeter = max([triangle[0] + triangle[1] + triangle[2] for triangle in triangle_list])

    # Calculate the minimum rod length
    min_rod_length = (total_area / max_perimeter) + 2

    return min_rod_length

