
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def closest_tree(x_b, y_b, x1, y1, x2, y2):
    closest_x = min(max(x1, x_b), x2)
    closest_y = min(max(y1, y_b), y2)
    return closest_x, closest_y

def can_see_belle(x_b, y_b, x1, y1, x2, y2):
    if x_b >= x1 and x_b <= x2 and y_b >= y1 and y_b <= y2:
        return "Yes"
    
    closest_x, closest_y = closest_tree(x_b, y_b, x1, y1, x2, y2)
    if distance(0, 0, closest_x, closest_y) < distance(0, 0, x_b, y_b):
        return "No\n{} {}".format(closest_x, closest_y)
    else:
        return "Yes"

if __name__ == "__main__":
    x_b, y_b = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    print(can_see_belle(x_b, y_b, x1, y1, x2, y2))
