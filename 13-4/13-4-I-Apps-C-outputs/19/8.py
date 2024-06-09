
def get_largest_corn_area(polygon, canal):
    # Find the area of the polygon
    area = get_polygon_area(polygon)
    
    # Find the area of the polygon on one side of the canal
    area_one_side = get_polygon_area_one_side(polygon, canal)
    
    # Find the area of the polygon on the other side of the canal
    area_other_side = area - area_one_side
    
    # Return the largest area
    return max(area_one_side, area_other_side)

def get_polygon_area(polygon):
    # Initialize the area
    area = 0
    
    # Iterate through the vertices
    for i in range(len(polygon)):
        # Calculate the area of the triangle
        area += (polygon[i][0] * polygon[(i+1) % len(polygon)][1]) - (polygon[i][1] * polygon[(i+1) % len(polygon)][0])
    
    # Return the absolute value of the area
    return abs(area / 2)

def get_polygon_area_one_side(polygon, canal):
    # Initialize the area
    area = 0
    
    # Iterate through the vertices
    for i in range(len(polygon)):
        # Check if the vertex is on the same side of the canal as the next vertex
        if is_same_side(polygon[i], polygon[(i+1) % len(polygon)], canal):
            # Calculate the area of the triangle
            area += (polygon[i][0] * polygon[(i+1) % len(polygon)][1]) - (polygon[i][1] * polygon[(i+1) % len(polygon)][0])
    
    # Return the absolute value of the area
    return abs(area / 2)

def is_same_side(p1, p2, canal):
    # Calculate the direction of the line segment
    direction = (p2[0] - p1[0]) * (canal[3] - canal[1]) - (p2[1] - p1[1]) * (canal[2] - canal[0])
    
    # Check if the line segment is on the same side of the canal as the point
    if direction > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    polygon = []
    canal = []
    
    # Read the input
    N = int(input())
    for i in range(N):
        x, y = map(int, input().split())
        polygon.append([x, y])
    xa, ya, xb, yb = map(int, input().split())
    canal = [xa, ya, xb, yb]
    
    # Calculate the largest corn area
    largest_corn_area = get_largest_corn_area(polygon, canal)
    
    # Print the result
    print(largest_corn_area)

