
import math

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
            if segment1[0] == segment2[0] and segment1[1] == segment2[1]:
                continue
            elif segment1[0] == segment2[0]:
                m = (segment1[1] - segment2[1]) / (segment1[0] - segment2[0])
                b = segment1[1] - m * segment1[0]
                x = segment1[0]
                y = m * x + b
                intersections.add((x, y))
            elif segment1[1] == segment2[1]:
                m = (segment1[0] - segment2[0]) / (segment1[1] - segment2[1])
                b = segment1[0] - m * segment1[1]
                x = segment1[1]
                y = m * x + b
                intersections.add((x, y))
            else:
                m1 = (segment1[1] - segment1[0]) / (segment1[0] - segment2[0])
                m2 = (segment2[1] - segment2[0]) / (segment1[0] - segment2[0])
                b1 = segment1[1] - m1 * segment1[0]
                b2 = segment2[1] - m2 * segment2[0]
                x = (b2 - b1) / (m1 - m2)
                y = m1 * x + b1
                intersections.add((x, y))
    
    # Find the regions by connecting the intersection points with line segments
    regions = set()
    for intersection in intersections:
        x, y = intersection
        for segment in segments:
            if segment[0] == x and segment[1] == y:
                regions.add(segment)
                break
    
    return len(regions)

n = int(input())
circles = []
for i in range(n):
    x, y, r = map(int, input().split())
    circles.append((x, y, r))

print(solve(n, circles))

