
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def area_triangle(p1, p2, p3):
    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p3, p1)
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def area_covered(pine_trees, aspen_trees):
    total_area = 0
    for i in range(len(pine_trees)):
        for j in range(i + 1, len(pine_trees)):
            for k in range(j + 1, len(pine_trees)):
                area = area_triangle(pine_trees[i], pine_trees[j], pine_trees[k])
                total_area += area

    for i in range(len(aspen_trees)):
        for j in range(i + 1, len(aspen_trees)):
            for k in range(j + 1, len(aspen_trees)):
                area = area_triangle(aspen_trees[i], aspen_trees[j], aspen_trees[k])
                total_area += area

    return total_area

if __name__ == "__main__":
    P, A = map(int, input().split())
    pine_trees = [tuple(map(float, input().split())) for _ in range(P)]
    aspen_trees = [tuple(map(float, input().split())) for _ in range(A)]

    result = area_covered(pine_trees, aspen_trees)
    print("{:.3f}".format(result))
