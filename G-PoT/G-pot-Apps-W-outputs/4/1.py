
from fractions import Fraction

def count_good_lines(points):
    n = len(points)
    if n == 1:
        return -1

    good_lines = set()
    for i in range(n):
        slopes = set()
        for j in range(n):
            if i != j:
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if dx == 0:
                    slope = float('inf')
                else:
                    slope = Fraction(dy, dx)
                slopes.add(slope)
        
        if len(slopes) == 1:
            good_lines.add(slopes.pop())

    if len(good_lines) == 0:
        return -1
    else:
        return len(good_lines)

# Read input
n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

# Calculate and print output
result = count_good_lines(points)
print(result)
