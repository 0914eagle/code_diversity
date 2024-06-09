
def get_maximum_circumference(vertices):
    
    # Calculate the area of the polygon
    area = get_polygon_area(vertices)
    
    # Calculate the maximum circumference of a hexagon that can be built
    max_circumference = 2 * math.sqrt(area / 3)
    
    return max_circumference

def get_polygon_area(vertices):
    
    # Calculate the area of the polygon using the shoelace formula
    area = 0
    for i in range(len(vertices)):
        j = (i + 1) % len(vertices)
        area += vertices[i][0] * vertices[j][1] - vertices[j][0] * vertices[i][1]
    area = abs(area) / 2
    
    return area

