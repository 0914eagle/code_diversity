
def f1(n, s):
    # find the convex hull of the Nazi troop positions
    hull = []
    hull.append((0, 0))
    for i in range(n):
        while len(hull) > 1 and not is_left(hull[-2], hull[-1], (x[i], y[i])):
            hull.pop()
        hull.append((x[i], y[i]))
    hull.append((0, 0))
    
    # check which castles are in danger
    in_danger = 0
    for i in range(s):
        if is_inside(hull, (x_castle[i], y_castle[i])):
            in_danger += 1
    
    return in_danger

def is_left(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) > 0

def is_inside(hull, p):
    n = len(hull)
    inside = False
    for i in range(n):
        if is_left(hull[i], hull[(i + 1) % n], p):
            inside = not inside
    return inside

if __name__ == '__main__':
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x.append(int(input()))
        y.append(int(input()))
    s = int(input())
    x_castle = []
    y_castle = []
    for i in range(s):
        x_castle.append(int(input()))
        y_castle.append(int(input()))
    print(f1(n, s))

