
import math

def check_collision(x1, y1, x2, y2, r):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if distance <= 2 * r:
        return True
    return False

def calculate_shot(w, l, r, x1, y1, x2, y2, x3, y3, h):
    if check_collision(x1, y1, x2, y2, r) and check_collision(x1, y1, x3, y3, r):
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return round(distance, 2), round(angle, 2)
    return "impossible"

# Input
w, l = map(int, input().split())
r, x1, y1, x2, y2, x3, y3, h = map(int, input().split())

# Output
result = calculate_shot(w, l, r, x1, y1, x2, y2, x3, y3, h)
print(result)
