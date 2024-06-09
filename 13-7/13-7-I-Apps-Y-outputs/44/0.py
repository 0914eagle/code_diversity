
def get_min_rod_length(triangle_list):
    
    # Calculate the sum of the areas of all the triangles
    total_area = sum([triangle_area(triangle) for triangle in triangle_list])

    # Calculate the minimum length of the rod required to hold all the triangles
    min_rod_length = (total_area / 2) ** 0.5

    return min_rod_length

def triangle_area(triangle):
    
    # Calculate the semi-perimeter of the triangle
    semi_perimeter = (triangle[0] + triangle[1] + triangle[2]) / 2

    # Calculate the area of the triangle
    area = semi_perimeter * (semi_perimeter - triangle[0]) * (semi_perimeter - triangle[1]) * (semi_perimeter - triangle[2])

    return area

