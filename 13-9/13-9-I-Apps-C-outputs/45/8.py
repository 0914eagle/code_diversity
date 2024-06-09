
import math

def convex_polygon(n):
    # Validate input
    if n < 3 or n > 400000:
        raise ValueError("Number of vertices must be between 3 and 400000")

    # Initialize list to store vertices
    vertices = []

    # Iterate through all possible combinations of x and y coordinates
    for x in range(0, 40000001):
        for y in range(0, 40000001):
            # Check if current combination is a valid vertex
            if is_valid_vertex(x, y, n, vertices):
                # Add vertex to list
                vertices.append((x, y))
                # If list has required number of vertices, return it
                if len(vertices) == n:
                    return vertices

    # If no valid combination is found, return empty list
    return []

# Check if a given vertex is valid
def is_valid_vertex(x, y, n, vertices):
    # Check if vertex is on a lattice point
    if x % 1 != 0 or y % 1 != 0:
        return False

    # Check if vertex is within required range
    if x < 0 or x > 40000000 or y < 0 or y > 40000000:
        return False

    # Check if vertex is not collinear with any other vertex
    for vertex in vertices:
        if are_collinear(vertex, (x, y)):
            return False

    # Check if vertex forms a convex polygon with existing vertices
    for i in range(n):
        if not is_convex(vertices[i], (x, y), vertices[(i+1) % n]):
            return False

    return True

# Check if two points are collinear
def are_collinear(p1, p2):
    return p1[0] * p2[1] == p1[1] * p2[0]

# Check if a point is on the left side of a line
def is_left(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) > (p3[0] - p1[0]) * (p2[1] - p1[1])

# Check if a point is on the same line as a line segment
def is_on_segment(p1, p2, p3):
    return is_left(p1, p2, p3) and is_left(p2, p1, p3)

# Check if a point is inside a convex polygon
def is_convex(p1, p2, p3):
    return is_on_segment(p1, p2, p3) or is_left(p1, p2, p3) != is_left(p1, p3, p2)

print(convex_polygon(int(input())))

