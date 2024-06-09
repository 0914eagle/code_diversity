
import math

def get_shared_area(pine_trees, aspen_trees):
    total_area = 0
    for pine_tree in pine_trees:
        for aspen_tree in aspen_trees:
            distance = math.sqrt((pine_tree[0] - aspen_tree[0]) ** 2 + (pine_tree[1] - aspen_tree[1]) ** 2)
            if distance <= 1:
                total_area += 1
    return total_area

def solve(input_lines):
    pine_trees = []
    aspen_trees = []
    for line in input_lines:
        x, y = line.split()
        x = float(x)
        y = float(y)
        if x == 0 and y == 0:
            break
        if x == 0:
            aspen_trees.append((x, y))
        elif y == 0:
            pine_trees.append((x, y))
        else:
            pine_trees.append((x, y))
            aspen_trees.append((x, y))
    return get_shared_area(pine_trees, aspen_trees)

