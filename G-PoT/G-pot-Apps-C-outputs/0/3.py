
import math

def check_collision(x1, y1, x2, y2, r):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if distance <= 2*r:
        return True
    else:
        return False

def solve_trick_shot(w, l, r, x1, y1, x2, y2, x3, y3, h):
    if check_collision(x1, y1, x2, y2, r) and check_collision(x1, y1, x3, y3, r):
        return "impossible"
    
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) - 2*r
    theta = math.degrees(math.atan2(y2 - y1, x2 - x1))
    
    return "{:.2f} {:.2f}".format(d, theta)

# Input
w, l = map(int, input().split())
r, x1, y1, x2, y2, x3, y3, h = map(int, input().split())

# Output
print(solve_trick_shot(w, l, r, x1, y1, x2, y2, x3, y3, h))
