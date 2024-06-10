
def get_cost(A, B):
    # Find the convex hull of the two polygons
    hull_A = convex_hull(A)
    hull_B = convex_hull(B)
    
    # Find the intersection of the two convex hulls
    intersection = set(hull_A).intersection(hull_B)
    
    # Calculate the cost of cutting out the intersection
    cost = 0
    for i in range(len(intersection)):
        cost += distance(intersection[i], intersection[(i+1)%len(intersection)])
    
    return cost

def convex_hull(points):
    # Sort the points by their x-coordinate
    sorted_points = sorted(points, key=lambda x: x[0])
    
    # Find the lower hull
    lower_hull = []
    for i in range(len(sorted_points)):
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], sorted_points[i]) <= 0:
            lower_hull.pop()
        lower_hull.append(sorted_points[i])
    
    # Find the upper hull
    upper_hull = []
    for i in range(len(sorted_points)-1, -1, -1):
        while len(upper_hull) >= 2 and cross_product(upper_hull[-2], upper_hull[-1], sorted_points[i]) <= 0:
            upper_hull.pop()
        upper_hull.append(sorted_points[i])
    
    # Combine the lower and upper hulls
    hull = lower_hull[:-1] + upper_hull[:-1]
    
    return hull

def cross_product(p1, p2, p3):
    return (p1[0] - p2[0]) * (p3[1] - p2[1]) - (p1[1] - p2[1]) * (p3[0] - p2[0])

def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

if __name__ == '__main__':
    # Read input
    A = []
    B = []
    for i in range(int(input())):
        x, y = map(int, input().split())
        A.append((x, y))
    for i in range(int(input())):
        x, y = map(int, input().split())
        B.append((x, y))
    
    # Calculate cost
    cost = get_cost(A, B)
    
    # Print output
    print("%.9f" % cost)

