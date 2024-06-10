
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def closest_blocking_tree(x_b, y_b, x1, y1, x2, y2):
    closest_tree = None
    min_distance = float('inf')
    
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if x == x_b and y == y_b:
                continue
            dist = distance(x, y, x_b, y_b)
            if dist < min_distance:
                min_distance = dist
                closest_tree = (x, y)
    
    return closest_tree

def can_see_belle(x_b, y_b, x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if x == x_b and y == y_b:
                continue
            if x == 0 and y == 0:
                continue
            if (y - y_b) * x == (x - x_b) * y:
                return "No\n{} {}".format(x, y)
    
    return "Yes"

if __name__ == "__main__":
    x_b, y_b = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    
    result = can_see_belle(x_b, y_b, x1, y1, x2, y2)
    print(result)
