
def solve(nazis, castles):
    # Convert lists of coordinates to sets of points
    nazi_points = set(tuple(coords) for coords in nazis)
    castle_points = set(tuple(coords) for coords in castles)
    
    # Initialize the number of in-danger castles to 0
    in_danger_castles = 0
    
    # Iterate over each castle
    for castle in castle_points:
        # Find the nearest three Nazi troops to the castle
        nearest_nazis = sorted(nazi_points, key=lambda point: distance(point, castle))[:3]
        
        # Check if the nearest three Nazi troops form a non-degenerate quadrilateral
        if is_non_degenerate_quadrilateral(nearest_nazis):
            # Increment the number of in-danger castles
            in_danger_castles += 1
    
    return in_danger_castles

def distance(point1, point2):
    # Calculate the Euclidean distance between two points
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def is_non_degenerate_quadrilateral(points):
    # Check if the four points form a non-degenerate quadrilateral
    return not (collinear(points[0], points[1], points[2]) or intersect(points[0], points[1], points[2], points[3]))

def collinear(point1, point2, point3):
    # Check if three points are collinear
    return point1[0] * (point2[1] - point3[1]) + point2[0] * (point3[1] - point1[1]) + point3[0] * (point1[1] - point2[1]) == 0

def intersect(line1, line2, line3, line4):
    # Check if two lines intersect
    def ccw(A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])
    
    return ccw(line1, line2, line3) != ccw(line1, line2, line4) and ccw(line3, line4, line1) != ccw(line3, line4, line2)

