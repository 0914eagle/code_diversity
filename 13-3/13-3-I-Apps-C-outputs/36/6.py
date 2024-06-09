
def solve(nazis, castles):
    # Convert lists of x and y coordinates to a set of points
    nazi_points = set([(x, y) for x, y in nazis])
    castle_points = set([(x, y) for x, y in castles])
    
    # Initialize a counter for the number of in-danger castles
    in_danger_castles = 0
    
    # Iterate over each castle point
    for castle in castle_points:
        # Find the nearest four Nazi points to the castle
        nearest_nazis = sorted(nazi_points, key=lambda point: distance(point, castle))[:4]
        
        # Check if the nearest four Nazi points form a non-degenerate quadrilateral
        if is_non_degenerate_quadrilateral(nearest_nazis):
            in_danger_castles += 1
    
    return in_danger_castles

def distance(point1, point2):
    # Calculate the Euclidean distance between two points
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def is_non_degenerate_quadrilateral(points):
    # Check if the four points form a non-degenerate quadrilateral
    return not collinear(points[0], points[1], points[2]) and not collinear(points[1], points[2], points[3]) and not intersecting(points[0], points[1], points[2], points[3])

def collinear(point1, point2, point3):
    # Check if three points are collinear
    return point1[0] * (point2[1] - point3[1]) + point2[0] * (point3[1] - point1[1]) + point3[0] * (point1[1] - point2[1]) == 0

def intersecting(point1, point2, point3, point4):
    # Check if the edges of two quadrilaterals intersect
    return (point1[0] - point2[0]) * (point3[1] - point4[1]) != (point1[1] - point2[1]) * (point3[0] - point4[0])

