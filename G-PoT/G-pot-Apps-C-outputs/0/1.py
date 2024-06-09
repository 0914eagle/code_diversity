
import math

def check_collision(x1, y1, x2, y2, r):
    return (x1 - x2)**2 + (y1 - y2)**2 <= (2*r)**2

def calculate_angle(x1, y1, x2, y2):
    return math.degrees(math.atan2(y2 - y1, x2 - x1))

def solve_trick_shot(w, l, r, x1, y1, x2, y2, x3, y3, h):
    if check_collision(x1, y1, x2, y2, r) and check_collision(x2, y2, x3, y3, r):
        d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        theta = calculate_angle(x1, y1, x2, y2)
        return round(d, 2), round(theta, 2)
    else:
        return "impossible"

# Input
w, l = map(int, input().split())
r, x1, y1, x2, y2, x3, y3, h = map(int, input().split())

# Output
result = solve_trick_shot(w, l, r, x1, y1, x2, y2, x3, y3, h)
print(result)
