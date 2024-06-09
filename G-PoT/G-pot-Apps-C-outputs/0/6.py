
import math

def check_collision(x1, y1, x2, y2, r):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance <= 2*r

def solve_trick_shot(w, l, r, x1, y1, x2, y2, x3, y3, h):
    if check_collision(x1, y1, x2, y2, r) and check_collision(x1, y1, x3, y3, r):
        angle = math.atan2(y2 - y1, x2 - x1)
        angle_degrees = math.degrees(angle)
        distance = math.sqrt((x1 - w/2)**2 + h**2)
        return round(distance, 2), round(angle_degrees, 2)
    else:
        return "impossible"

# Input
w, l = map(int, input().split())
r, x1, y1, x2, y2, x3, y3, h = map(int, input().split())

# Solve trick shot
result = solve_trick_shot(w, l, r, x1, y1, x2, y2, x3, y3, h)

# Output
if result == "impossible":
    print("impossible")
else:
    print(*result)
