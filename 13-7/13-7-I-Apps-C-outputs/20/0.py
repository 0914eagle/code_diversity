
def solve(pine_trees, aspen_trees):
    # Calculate the area covered by both species
    area = 0
    for pine in pine_trees:
        for aspen in aspen_trees:
            if is_covered_by_both(pine, aspen):
                area += triangle_area(pine, aspen)
    return area

def is_covered_by_both(tree1, tree2):
    # Check if the triangle formed by the three trees is covered by both species
    return (tree1[0] == tree2[0] or tree1[1] == tree2[1] or tree1[0] + tree1[1] == tree2[0] + tree2[1]) and (tree1[0] == tree2[0] or tree1[1] == tree2[1] or tree1[0] + tree1[1] == tree2[0] + tree2[1])

def triangle_area(tree1, tree2):
    # Calculate the area of the triangle formed by the three trees
    area = 0.5 * abs(tree1[0] * tree2[1] - tree1[1] * tree2[0])
    return area

