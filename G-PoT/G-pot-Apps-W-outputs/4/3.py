
from collections import defaultdict

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def count_good_lines(points):
    n = len(points)
    good_lines = set()
    
    for i in range(n):
        slopes = defaultdict(int)
        same_points = 0
        
        for j in range(n):
            if i != j:
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                if dx == 0 and dy == 0:
                    same_points += 1
                else:
                    g = gcd(abs(dx), abs(dy))
                    slope = (dx // g, dy // g)
                    slopes[slope] += 1
        
        max_count = max(slopes.values()) if slopes else 0
        good_lines.add((same_points, max_count))
    
    if any(same_points == n - 1 for same_points, _ in good_lines):
        return -1
    
    return sum(count for _, count in good_lines)

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
print(count_good_lines(points))
