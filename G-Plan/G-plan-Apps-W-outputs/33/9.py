
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def closest_tree(x, y, x1, y1, x2, y2):
    closest_x = max(x1, min(x, x2))
    closest_y = max(y1, min(y, y2))
    return closest_x, closest_y

def can_see_belle(x_b, y_b, x1, y1, x2, y2):
    if x_b < x1 or x_b > x2 or y_b < y1 or y_b > y2:
        return "Yes"
    
    closest_x, closest_y = closest_tree(x_b, y_b, x1, y1, x2, y2)
    if (closest_x, closest_y) == (x_b, y_b):
        return "Yes"
    else:
        return f"No\n{closest_x} {closest_y}"

if __name__ == "__main__":
    x_b, y_b = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    print(can_see_belle(x_b, y_b, x1, y1, x2, y2))
