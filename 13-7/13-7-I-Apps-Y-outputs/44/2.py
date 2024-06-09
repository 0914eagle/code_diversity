
import math

def get_min_rod_length(triangles):
    
    # Calculate the sum of the areas of all triangles
    area_sum = 0
    for triangle in triangles:
        area_sum += get_triangle_area(triangle)

    # Calculate the perimeter of the largest triangle
    max_perimeter = 0
    for triangle in triangles:
        perimeter = get_triangle_perimeter(triangle)
        if perimeter > max_perimeter:
            max_perimeter = perimeter

    # Calculate the minimum required length for the rod
    rod_length = (area_sum * 2) / max_perimeter

    return rod_length

def get_triangle_area(triangle):
    
    a, b, c = triangle
    semi_perimeter = (a + b + c) / 2
    area = math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))
    return area

def get_triangle_perimeter(triangle):
    
    a, b, c = triangle
    perimeter = a + b + c
    return perimeter

triangles = [[3, 3, 3], [4, 4, 5]]
print(get_min_rod_length(triangles))

