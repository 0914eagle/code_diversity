
def get_input():
    return int(input())

def is_convex(vertices):
    # Check if the polygon is convex
    for i in range(len(vertices)):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % len(vertices)]
        v3 = vertices[(i + 2) % len(vertices)]
        if not is_angle_convex(v1, v2, v3):
            return False
    return True

def is_angle_convex(v1, v2, v3):
    # Check if the angle formed by v1, v2, v3 is convex
    return (v1[0] - v2[0]) * (v3[1] - v2[1]) - (v1[1] - v2[1]) * (v3[0] - v2[0]) >= 0

def get_diagonals(vertices):
    # Get all diagonals in the polygon
    diagonals = []
    for i in range(len(vertices)):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % len(vertices)]
        diagonals.append((v1, v2))
    return diagonals

def count_intersections(diagonals):
    # Count the number of intersections between pairs of diagonals
    count = 0
    for i in range(len(diagonals)):
        for j in range(i + 1, len(diagonals)):
            d1 = diagonals[i]
            d2 = diagonals[j]
            if do_intersect(d1, d2):
                count += 1
    return count

def do_intersect(d1, d2):
    # Check if two diagonals intersect
    x1, y1 = d1[0]
    x2, y2 = d1[1]
    x3, y3 = d2[0]
    x4, y4 = d2[1]
    return (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4) != 0 and (x1 - x3) * (y2 - y4) - (y1 - y3) * (x2 - x4) != 0

def main():
    N = get_input()
    vertices = [(0, 0)]
    for i in range(N):
        x, y = map(int, input().split())
        vertices.append((x, y))
    if not is_convex(vertices):
        print(0)
        return
    diagonals = get_diagonals(vertices)
    print(count_intersections(diagonals))

if __name__ == '__main__':
    main()

