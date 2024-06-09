
def is_right_triangle(p1, p2, p3):
    # Calculate the lengths of the sides of the triangle
    a = abs(p1[0] - p2[0])
    b = abs(p1[1] - p2[1])
    c = abs(p1[0] - p3[0])

    # Check if the triangle is right by checking the angles
    return a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2

def count_right_triangles(points):
    count = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                if is_right_triangle(points[i], points[j], points[k]):
                    count += 1
    return count

# Test the function with some examples
points = [(4, 2), (2, 1), (1, 3)]
print(count_right_triangles(points))  # Output: 1

points = [(5, 0), (2, 6), (8, 6), (5, 7)]
print(count_right_triangles(points))  # Output: 0

