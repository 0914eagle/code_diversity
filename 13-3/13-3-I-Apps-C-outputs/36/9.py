
def solve(nazis, castles):
    # Step 1: Sort the Nazi points by x-coordinate
    nazis = sorted(nazis, key=lambda x: x[0])
    
    # Step 2: Find the convex hull of the Nazi points
    hull = []
    for p in nazis:
        while len(hull) > 1 and cross_product(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    
    # Step 3: Count the number of castles in danger
    count = 0
    for c in castles:
        if is_inside_convex_polygon(c, hull):
            count += 1
    
    return count

def cross_product(o, a, b):
    # Cross product of two vectors
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def is_inside_convex_polygon(p, polygon):
    # Check if a point is inside a convex polygon
    c = 0
    for i in range(len(polygon) - 1):
        if polygon[i][1] <= p[1]:
            if polygon[i + 1][1] > p[1]:
                if cross_product(polygon[i], polygon[i + 1], p) > 0:
                    c += 1
        elif polygon[i + 1][1] <= p[1]:
            if cross_product(polygon[i], polygon[i + 1], p) < 0:
                c -= 1
    return c != 0

