
def count_triangles(sides):
    # Calculate the perimeter of the hexagon
    perimeter = sum(sides)
    
    # Calculate the number of triangles
    num_triangles = perimeter // 3
    
    return num_triangles

