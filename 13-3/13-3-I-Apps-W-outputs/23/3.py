
def solve(n, a):
    # Initialize the list of vertices
    vertices = list(range(1, n+1))
    # Initialize the minimum difference between the angle and a as infinity
    min_diff = float('inf')
    # Initialize the optimal vertices as empty list
    optimal_vertices = []
    # Iterate over all possible combinations of three vertices
    for v1, v2, v3 in combinations(vertices, 3):
        # Calculate the angle between the three vertices
        angle = angle_between_vertices(v1, v2, v3)
        # Calculate the difference between the angle and a
        diff = abs(angle - a)
        # If the difference is less than the minimum difference, update the minimum difference and the optimal vertices
        if diff < min_diff:
            min_diff = diff
            optimal_vertices = [v1, v2, v3]
    # Return the optimal vertices
    return optimal_vertices

# Calculate the angle between three vertices
def angle_between_vertices(v1, v2, v3):
    # Calculate the sides of the triangle
    a = distance(v1, v2)
    b = distance(v2, v3)
    c = distance(v3, v1)
    # Calculate the semi-perimeter of the triangle
    s = (a + b + c) / 2
    # Calculate the area of the triangle
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    # Calculate the angle between the three vertices
    angle = degrees(acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
    return angle

# Calculate the distance between two points
def distance(v1, v2):
    return ((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2) ** 0.5

