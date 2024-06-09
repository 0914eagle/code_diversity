
def solve(pine_trees, aspen_trees):
    # Calculate the area covered by both species
    area = 0
    for pine in pine_trees:
        for aspen in aspen_trees:
            if is_covered(pine, aspen):
                area += triangle_area(pine, aspen)
    return area

def is_covered(tree1, tree2):
    # Check if a point is covered by a triangle made by three distinct trees
    x1, y1 = tree1
    x2, y2 = tree2
    return (x1 <= x2 <= y1) and (x2 <= y1 <= y2) and (x1 <= y2 <= y1)

def triangle_area(tree1, tree2):
    # Calculate the area of a triangle
    x1, y1 = tree1
    x2, y2 = tree2
    return 0.5 * abs(x1 * y2 - x2 * y1)

