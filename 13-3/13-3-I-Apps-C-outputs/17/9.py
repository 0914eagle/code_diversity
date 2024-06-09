
def get_shared_area(pine_trees, aspen_trees):
    total_area = 0
    for pine_tree in pine_trees:
        for aspen_tree in aspen_trees:
            area = get_triangle_area(pine_tree, aspen_tree)
            total_area += area
    return total_area

def get_triangle_area(tree1, tree2):
    x1, y1 = tree1
    x2, y2 = tree2
    area = 0.5 * abs(x1*y2 + x2*y1 + x1*y1 - x2*y2 - x1*y2 - x2*y1)
    return area

pine_trees = [(0.0, 6.0), (6.0, 0.0), (6.0, 6.0)]
aspen_trees = [(4.0, 4.0), (10.0, 4.0), (4.0, 10.0)]
print(get_shared_area(pine_trees, aspen_trees))

