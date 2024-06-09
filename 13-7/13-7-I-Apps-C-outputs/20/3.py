
import math

def get_area_covered(pine_trees, aspen_trees):
    area = 0
    for pine_tree in pine_trees:
        for aspen_tree in aspen_trees:
            area += get_triangle_area(pine_tree, aspen_tree)
    return area

def get_triangle_area(tree1, tree2):
    x1, y1 = tree1
    x2, y2 = tree2
    return 0.5 * math.fabs(x1*y2 + x2*y1 + x2*y1 - x1*y2 - x2*y2 - x1*y1)

def solve(pine_trees, aspen_trees):
    return get_area_covered(pine_trees, aspen_trees)

