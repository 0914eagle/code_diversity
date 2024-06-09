
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def count_good_lines(points):
    n = len(points)
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
                    gcd_val = gcd(abs(dx), abs(dy))
                    slope = (dy // gcd_val, dx // gcd_val)
                slopes.add(slope)
        
        if len(slopes) == 1:
            good_lines.add(slopes.pop())

    if len(good_lines) == 0:
        return -1
    elif len(good_lines) == 1 and (0, 0) in good_lines:
        return -1
    else:
        return len(good_lines)

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

result = count_good_lines(points)
print(result)
