
import math

def calculate_distance_and_angle(w, l, r, x1, y1, x2, y2, x3, y3, h):
    def distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def angle(x1, y1, x2, y2):
        return math.degrees(math.atan2(y2 - y1, x2 - x1))

    d = (x2 - x1) / 2
    theta1 = angle(x1, y1, x2, y2)
    theta2 = angle(x2, y2, x3, y3)

    if distance(x1, y1, x2, y2) <= 2 * r and distance(x2, y2, x3, y3) <= 2 * r:
        return round(d, 2), round(theta1, 2)
    else:
        return "impossible"

# Input
w, l = map(int, input().split())
r, x1, y1, x2, y2, x3, y3, h = map(int, input().split())

# Output
result = calculate_distance_and_angle(w, l, r, x1, y1, x2, y2, x3, y3, h)
print(result)
