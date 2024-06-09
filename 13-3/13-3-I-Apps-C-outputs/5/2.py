
def solve(n, q, x, y, a, b):
    # Convert the input coordinates into a set of points
    points = set()
    for i in range(n):
        points.add((x[i], y[i]))
    
    # Initialize the minimum side length to infinity
    min_side_length = float('inf')
    
    # Iterate over each zoning request
    for i in range(q):
        # Find the minimum side length for the current request
        min_side_length_current = float('inf')
        for j in range(a[i], b[i] + 1):
            # Find the closest point to the current point
            closest_point = find_closest_point(points, (x[j], y[j]))
            # Update the minimum side length if necessary
            min_side_length_current = min(min_side_length_current, distance(closest_point, (x[j], y[j])))
        
        # Update the global minimum side length
        min_side_length = min(min_side_length, min_side_length_current)
    
    # Return the minimum side length
    return min_side_length

def find_closest_point(points, point):
    # Initialize the closest point to the first point in the set
    closest_point = points.pop()
    
    # Iterate over the remaining points in the set
    for p in points:
        # If the current point is closer to the query point, update the closest point
        if distance(p, point) < distance(closest_point, point):
            closest_point = p
    
    # Return the closest point
    return closest_point

def distance(p1, p2):
    # Calculate the Euclidean distance between the two points
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

n, q = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(solve(n, q, x, y, a, b))

