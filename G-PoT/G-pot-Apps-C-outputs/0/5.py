
import math

def check_collision(x1, y1, x2, y2, r):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance <= 2 * r

def calculate_angle(x1, y1, x2, y2):
    return math.degrees(math.atan2(y2 - y1, x2 - x1))

def solve_trick_shot(w, l, r, x1, y1, x2, y2, x3, y3, h):
    if not check_collision(x1, y1, x2, y2, r):
        return "impossible"
    
    angle1 = calculate_angle(x1, y1, x2, y2)
    angle2 = calculate_angle(x2, y2, x3, y3)
    
    d = math.sqrt((x1 - 0) ** 2 + (l - y1) ** 2)
    theta = 180 - angle1 - angle2
    
    return f"{d:.2f} {theta:.2f}"

# Input
w, l = map(int, input().split())
r, x1, y1, x2, y2, x3, y3, h = map(int, input().split())

# Solve trick shot
result = solve_trick_shot(w, l, r, x1, y1, x2, y2, x3, y3, h)
print(result)
