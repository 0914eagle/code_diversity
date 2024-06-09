
import math

# Function to calculate the distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to calculate the angle between two points
def angle(x1, y1, x2, y2):
    return math.degrees(math.atan2(y2 - y1, x2 - x1))

# Function to check if the trick shot is possible
def is_trick_shot_possible(w, l, r, x1, y1, x2, y2, x3, y3, h):
    d = distance(x1, y1, x2, y2)
    theta = angle(x1, y1, x2, y2)
    
    if d < 2*r or d > w - 2*r or h - r < 0 or h + r > l:
        return "impossible"
    
    d2 = distance(x2, y2, x3, y3)
    theta2 = angle(x2, y2, x3, y3)
    
    if d2 < 2*r or d2 > w - 2*r or h - r < 0 or h + r > l:
        return "impossible"
    
    return f"{d:.2f} {theta:.2f}\n{d2:.2f} {theta2:.2f}"

# Input
w, l = map(int, input().split())
r, x1, y1, x2, y2, x3, y3, h = map(int, input().split())

# Check if trick shot is possible
result = is_trick_shot_possible(w, l, r, x1, y1, x2, y2, x3, y3, h)
print(result)
