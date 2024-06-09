
import math

def count_good_lines(n, points):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    def get_slope(x, y):
        if x == 0:
            return (0, 1)
        if y == 0:
            return (1, 0)
        g = gcd(abs(x), abs(y))
        return (x // g, y // g)
    
    slopes = set()
    for i in range(n):
        for j in range(i+1, n):
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            slope = get_slope(dx, dy)
            slopes.add(slope)
    
    if len(slopes) == 0:
        return -1
    return len(slopes)

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

result = count_good_lines(n, points)
print(result)
