
import math

def solve(n, circles):
    # Convert the circles to a set of line segments
    segments = []
    for circle in circles:
        x, y, r = circle
        segments.append([(x + r, y), (x - r, y)])
        segments.append([(x, y + r), (x, y - r)])
    
    # Sort the segments by their slope
    segments.sort(key=lambda segment: segment[0][1] - segment[1][1])
    
    # Count the number of regions
    regions = set()
    for segment in segments:
        x1, y1 = segment[0]
        x2, y2 = segment[1]
        if x1 == x2:
            continue
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        regions.add((m, b))
    
    return len(regions)

n = int(input())
circles = []
for i in range(n):
    x, y, r = map(int, input().split())
    circles.append((x, y, r))
print(solve(n, circles))

