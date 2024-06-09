
def solve(n, circles):
    # Convert the circles to a set of line segments
    segments = []
    for circle in circles:
        x, y, r = circle
        segments.append([(x + r, y), (x - r, y)])
        segments.append([(x, y + r), (x, y - r)])
    
    # Find the intersection points of the line segments
    intersections = []
    for i in range(len(segments)):
        for j in range(i + 1, len(segments)):
            intersection = find_intersection(segments[i], segments[j])
            if intersection is not None:
                intersections.append(intersection)
    
    # Sort the intersections by their x-coordinate
    intersections.sort(key=lambda x: x[0])
    
    # Find the number of regions by counting the number of intersections
    regions = 1
    for i in range(len(intersections)):
        if i > 0 and intersections[i][0] != intersections[i - 1][0]:
            regions += 1
    
    return regions

def find_intersection(segment1, segment2):
    (x1, y1), (x2, y2) = segment1
    (x3, y3), (x4, y4) = segment2
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return None
    x = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
    x = x / denom
    y = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
    y = y / denom
    return x, y

