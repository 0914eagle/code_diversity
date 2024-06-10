
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def triangle_area(p1, p2, p3):
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
                pine_area = triangle_area(pine_trees[i], pine_trees[j], pine_trees[k])
                for m in range(len(aspen_trees)):
                    for n in range(m + 1, len(aspen_trees)):
                        for o in range(n + 1, len(aspen_trees)):
                            aspen_area = triangle_area(aspen_trees[m], aspen_trees[n], aspen_trees[o])
                            common_area = min(pine_area, aspen_area)
                            total_area = max(total_area, common_area)
    return total_area

def parse_input():
    P, A = map(int, input().split())
    pine_trees = [tuple(map(float, input().split())) for _ in range(P)]
    aspen_trees = [tuple(map(float, input().split())) for _ in range(A)]
    return pine_trees, aspen_trees

if __name__ == "__main__":
    pine_trees, aspen_trees = parse_input()
    result = area_covered(pine_trees, aspen_trees)
    print("{:.3f}".format(result))
