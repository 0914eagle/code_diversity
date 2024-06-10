
import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_area(p1, p2, p3):
    a = calculate_distance(p1, p2)
    b = calculate_distance(p2, p3)
    c = calculate_distance(p3, p1)
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def find_shared_area(pine_trees, aspen_trees):
    shared_area = 0.0
    for i in range(len(pine_trees)):
        for j in range(i + 1, len(pine_trees)):
            for k in range(j + 1, len(pine_trees)):
                area_pine = calculate_area(pine_trees[i], pine_trees[j], pine_trees[k])
                for m in range(len(aspen_trees)):
                    for n in range(m + 1, len(aspen_trees)):
                        for o in range(n + 1, len(aspen_trees)):
                            area_aspen = calculate_area(aspen_trees[m], aspen_trees[n], aspen_trees[o])
                            shared_area = max(shared_area, min(area_pine, area_aspen))
    return shared_area

if __name__ == "__main__":
    P, A = map(int, input().split())
    pine_trees = [tuple(map(float, input().split())) for _ in range(P)]
    aspen_trees = [tuple(map(float, input().split())) for _ in range(A)]
    result = find_shared_area(pine_trees, aspen_trees)
    print("{:.3f}".format(result))
