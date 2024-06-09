
def solve(P, A, pine_locations, aspen_locations):
    # Calculate the area covered by both species
    area = 0
    
    # Iterate over each pine tree
    for pine in pine_locations:
        # Find the closest aspen tree
        closest_aspen = min(aspen_locations, key=lambda aspen: distance(pine, aspen))
        
        # Calculate the area of the triangle formed by the pine, aspen, and the origin
        triangle_area = triangle_area_2d(pine, closest_aspen, (0, 0))
        
        # Add the area to the total area
        area += triangle_area
    
    return area

def distance(point1, point2):
    return ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**0.5

def triangle_area_2d(point1, point2, point3):
    area = 0.5 * abs(point1[0] * (point2[1] - point3[1]) + point2[0] * (point3[1] - point1[1]) + point3[0] * (point1[1] - point2[1]))
    return area

