
def get_min_rod_length(triangle_list):
    
    # Calculate the sum of the areas of all the triangles
    total_area = sum([triangle_area(triangle) for triangle in triangle_list])

    # Calculate the minimum perimeter of all the triangles
    min_perimeter = min([triangle_perimeter(triangle) for triangle in triangle_list])

    # Calculate the minimum rod length based on the sum of the areas and minimum perimeter
    min_rod_length = (total_area / min_perimeter) + min_perimeter

    return min_rod_length

def triangle_area(triangle):
    
    a, b, c = triangle
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def triangle_perimeter(triangle):
    
    return sum(triangle)

