
def solve(n, a):
    # Initialize the list of vertices
    vertices = list(range(1, n+1))
    # Initialize the minimum difference between the angle and a as a large number
    min_diff = 1000
    # Initialize the optimal vertices as empty list
    opt_vertices = []
    # Iterate over all possible combinations of three vertices
    for v1 in vertices:
        for v2 in vertices:
            for v3 in vertices:
                # Calculate the angle between the three vertices
                angle = angle_between(v1, v2, v3)
                # Calculate the difference between the angle and a
                diff = abs(angle - a)
                # If the difference is smaller than the minimum difference, update the minimum difference and the optimal vertices
                if diff < min_diff:
                    min_diff = diff
                    opt_vertices = [v1, v2, v3]
    # Return the optimal vertices
    return opt_vertices

# Calculate the angle between three vertices
def angle_between(v1, v2, v3):
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

# Calculate the distance between two vertices
def distance(v1, v2):
    return abs(v1 - v2)

# Convert radians to degrees
def degrees(angle):
    return angle * 180 / 3.14

