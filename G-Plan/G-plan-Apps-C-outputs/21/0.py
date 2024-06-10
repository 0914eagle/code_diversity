
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_area(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))

def find_shared_area(pine_trees, aspen_trees):
    shared_area = 0.0
    for i in range(len(pine_trees)):
        for j in range(i + 1, len(pine_trees)):
            for k in range(j + 1, len(pine_trees)):
                area = calculate_area(pine_trees[i][0], pine_trees[i][1], pine_trees[j][0], pine_trees[j][1], pine_trees[k][0], pine_trees[k][1])
                shared_area = max(shared_area, area)
    
    for i in range(len(aspen_trees)):
        for j in range(i + 1, len(aspen_trees)):
            for k in range(j + 1, len(aspen_trees)):
                area = calculate_area(aspen_trees[i][0], aspen_trees[i][1], aspen_trees[j][0], aspen_trees[j][1], aspen_trees[k][0], aspen_trees[k][1])
                shared_area = max(shared_area, area)
    
    return shared_area

if __name__ == "__main__":
    P, A = map(int, input().split())
    pine_trees = [tuple(map(float, input().split())) for _ in range(P)]
    aspen_trees = [tuple(map(float, input().split())) for _ in range(A)]
    
    result = find_shared_area(pine_trees, aspen_trees)
    print("{:.3f}".format(result))
