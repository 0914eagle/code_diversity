
def get_input():
    return int(input())

def is_convex(vertices):
    # Check if all interior angles are less than 180 degrees
    for i in range(len(vertices)):
        angle = get_angle(vertices, i)
        if angle > 180:
            return False
    return True

def get_angle(vertices, i):
    # Get the angle between the ith vertex and its two neighbors
    v1 = vertices[i]
    v2 = vertices[(i + 1) % len(vertices)]
    v3 = vertices[(i + 2) % len(vertices)]
    return get_angle_between_points(v1, v2, v3)

def get_angle_between_points(p1, p2, p3):
    # Get the angle between three points in a 2D plane
    v1 = [p2[0] - p1[0], p2[1] - p1[1]]
    v2 = [p3[0] - p1[0], p3[1] - p1[1]]
    return get_angle_between_vectors(v1, v2)

def get_angle_between_vectors(v1, v2):
    # Get the angle between two vectors in a 2D plane
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    magnitude1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
    magnitude2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)
    cosine_angle = dot_product / (magnitude1 * magnitude2)
    return math.acos(cosine_angle) * 180 / math.pi

def find_intersections(vertices):
    # Find the number of intersections between pairs of diagonals
    intersections = 0
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            if do_intersect(vertices, i, j):
                intersections += 1
    return intersections

def do_intersect(vertices, i, j):
    # Check if the ith and jth diagonals intersect
    v1 = vertices[i]
    v2 = vertices[(i + 1) % len(vertices)]
    v3 = vertices[j]
    v4 = vertices[(j + 1) % len(vertices)]
    return do_segments_intersect(v1, v2, v3, v4)

def do_segments_intersect(p1, p2, p3, p4):
    # Check if two line segments intersect
    s1_x = p2[0] - p1[0]
    s1_y = p2[1] - p1[1]
    s2_x = p4[0] - p3[0]
    s2_y = p4[1] - p3[1]
    s = (-s1_y * (p1[0] - p3[0]) + s1_x * (p1[1] - p3[1])) / (-s2_x * s1_y + s1_x * s2_y)
    t = ( s2_x * (p1[1] - p3[1]) - s2_y * (p1[0] - p3[0])) / (-s2_x * s1_y + s1_x * s2_y)
    return s >= 0 and t >= 0 and s + t <= 1

def main():
    N = get_input()
    vertices = []
    for i in range(N):
        x, y = map(int, input().split())
        vertices.append([x, y])
    if is_convex(vertices):
        print(find_intersections(vertices))
    else:
        print("Not a convex polygon.")

if __name__ == '__main__':
    main()

