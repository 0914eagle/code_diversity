
def solve(nazis, castles):
    # Step 1: Find the convex hull of the Nazi positions
    hull = []
    for i in range(len(nazis)):
        if len(hull) == 0:
            hull.append(nazis[i])
        else:
            while len(hull) > 1 and not is_left(hull[-2], hull[-1], nazis[i]):
                hull.pop()
            hull.append(nazis[i])
    
    # Step 2: Check which castles are inside the convex hull
    in_danger = 0
    for castle in castles:
        if is_inside(hull, castle):
            in_danger += 1
    
    return in_danger

def is_left(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) > 0

def is_inside(hull, point):
    i = 0
    j = len(hull) - 1
    while i < len(hull) and not (hull[i][0] == point[0] and hull[i][1] == point[1]):
        if is_left(hull[i], hull[j], point):
            i += 1
        else:
            j -= 1
    return i <= j

