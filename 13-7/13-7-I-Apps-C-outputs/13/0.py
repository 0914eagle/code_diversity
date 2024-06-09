
def solve(n, circles):
    # Convert the input circles to a set of line segments
    segments = set()
    for circle in circles:
        x, y, r = circle
        segments.add((x + r, y))
        segments.add((x - r, y))
        segments.add((x, y + r))
        segments.add((x, y - r))
    
    # Find the intersection points of the line segments
    intersections = set()
    for i in range(len(segments)):
        for j in range(i + 1, len(segments)):
            segment1 = segments[i]
            segment2 = segments[j]
            x1, y1 = segment1[0], segment1[1]
            x2, y2 = segment2[0], segment2[1]
            if x1 == x2:
                continue
            m = (y2 - y1) / (x2 - x1)
            b = y1 - m * x1
            x = (b - y1) / (m - 1)
            y = m * x + b
            if x1 < x2:
                x = max(x1, x)
            else:
                x = min(x1, x)
            intersections.add((x, y))
    
    # Find the regions by connecting the intersection points with line segments
    regions = set()
    for intersection in intersections:
        x, y = intersection
        for segment in segments:
            x1, y1 = segment[0], segment[1]
            if x1 == x:
                continue
            m = (y - y1) / (x - x1)
            b = y - m * x
            x2 = (b - y1) / (m - 1)
            y2 = m * x2 + b
            regions.add((x1, y1, x2, y2))
    
    return len(regions)

