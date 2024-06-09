
def get_min_rod_length(triangle_list):
    
    # Calculate the area of each triangle
    areas = [triangle_area(triangle) for triangle in triangle_list]

    # Calculate the sum of the areas
    total_area = sum(areas)

    # Calculate the perimeter of the largest triangle
    max_perimeter = max(triangle_perimeter(triangle) for triangle in triangle_list)

    # Calculate the minimum required length for the rod
    min_rod_length = (total_area / max_perimeter) + max_perimeter

    return min_rod_length

def triangle_area(triangle):
    
    a, b, c = triangle
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

def triangle_perimeter(triangle):
    
    return sum(triangle)

