
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def angle(x1, y1, x2, y2):
    return math.degrees(math.atan2(y2 - y1, x2 - x1))

def is_possible(w, l, r, x1, y1, x2, y2, x3, y3, h):
    d_possible = False
    theta_possible = False

    d1 = distance(x1, y1, x2, y2) - 2 * r
    d2 = distance(x2, y2, x3, y3) - 2 * r

    if d1 >= 2 * r and d2 >= 2 * r:
        d_possible = True

    if y1 > h + r and y2 > l - h - r and y3 > l - h - r:
        theta_possible = True

    if d_possible and theta_possible:
        d = round(d1, 2)
        theta = round(angle(x1, y1, x2, y2), 2)
        return d, theta
    else:
        return "impossible"

w, l = map(int, input().split())
r, x1, y1, x2, y2, x3, y3, h = map(int, input().split())

result = is_possible(w, l, r, x1, y1, x2, y2, x3, y3, h)
if result != "impossible":
    print(result[0], result[1])
else:
    print("impossible")
