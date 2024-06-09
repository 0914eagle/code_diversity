
def get_shared_area(pine_trees, aspen_trees):
    pine_tree_coords = [(x, y) for x, y in pine_trees]
    aspen_tree_coords = [(x, y) for x, y in aspen_trees]
    total_area = 0
    for pine_tree in pine_tree_coords:
        for aspen_tree in aspen_tree_coords:
            area = get_triangle_area(pine_tree, aspen_tree)
            total_area += area
    return total_area

def get_triangle_area(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return 0.5 * abs(x1 * y2 - x2 * y1)

