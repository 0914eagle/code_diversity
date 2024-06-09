
import math

def solve(n, circles):
    # Convert the input circles to a set of line segments
    segments = []
    for circle in circles:
        x, y, r = circle
        segments.append([(x + r, y), (x - r, y)])
        segments.append([(x, y + r), (x, y - r)])
    
    # Sort the segments by their slope
    segments.sort(key=lambda segment: segment[0][1] - segment[1][1])
    
    # Initialize the number of regions as 0
    regions = 0
    
    # Iterate through the segments and count the number of regions
    for segment in segments:
        x1, y1 = segment[0]
        x2, y2 = segment[1]
        if x1 == x2:
            # Horizontal segment, ignore
            continue
        else:
            # Calculate the slope and y-intercept of the segment
            m = (y2 - y1) / (x2 - x1)
            b = y1 - m * x1
            
            # Check if the segment intersects with any of the other segments
            for other_segment in segments:
                x3, y3 = other_segment[0]
                x4, y4 = other_segment[1]
                if x3 == x4:
                    # Horizontal segment, ignore
                    continue
                else:
                    # Calculate the slope and y-intercept of the other segment
                    m_other = (y4 - y3) / (x4 - x3)
                    b_other = y3 - m_other * x3
                    
                    # Check if the segments intersect
                    if m == m_other:
                        # Parallel segments, ignore
                        continue
                    else:
                        # Calculate the x-coordinate of intersection
                        x_intersect = (b_other - b) / (m - m_other)
                        
                        # Check if the intersection is between the endpoints of both segments
                        if x_intersect >= min(x1, x2) and x_intersect <= max(x1, x2) and x_intersect >= min(x3, x4) and x_intersect <= max(x3, x4):
                            # Increment the number of regions
                            regions += 1
    
    return regions

n = int(input())
circles = []
for i in range(n):
    x, y, r = map(int, input().split())
    circles.append([x, y, r])

regions = solve(n, circles)
print(regions)

