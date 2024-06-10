
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def closest_blocking_tree(x_b, y_b, x1, y1, x2, y2):
    closest_tree = None
    min_distance = float('inf')
    
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            dist = distance(x, y, x_b, y_b)
            if dist < min_distance:
                min_distance = dist
                closest_tree = (x, y)
    
    return closest_tree

def can_see_belle(x_b, y_b, x1, y1, x2, y2):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if x == x_b and y == y_b:
                return "Yes"
    
    closest_tree = closest_blocking_tree(x_b, y_b, x1, y1, x2, y2)
    return f"No\n{closest_tree[0]} {closest_tree[1]}"

if __name__ == "__main__":
    x_b, y_b = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    
    print(can_see_belle(x_b, y_b, x1, y1, x2, y2))
