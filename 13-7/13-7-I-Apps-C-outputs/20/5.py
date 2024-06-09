
def solve(pine_trees, aspen_trees):
    # Calculate the area of each species
    pine_area = 0
    aspen_area = 0
    for pine_tree in pine_trees:
        pine_area += triangle_area(pine_tree, aspen_trees)
    for aspen_tree in aspen_trees:
        aspen_area += triangle_area(aspen_tree, pine_trees)
    
    # Return the total area
    return pine_area + aspen_area

def triangle_area(tree, other_trees):
    area = 0
    for other_tree in other_trees:
        area += triangle_area_helper(tree, other_tree)
    return area

def triangle_area_helper(tree1, tree2):
    x1, y1 = tree1
    x2, y2 = tree2
    return 0.5 * abs(x1 * y2 - x2 * y1)

