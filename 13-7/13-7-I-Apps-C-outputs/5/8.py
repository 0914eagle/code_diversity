
def get_largest_connected_group(heights, growth_speeds):
    # Initialize a dictionary to store the tree heights and their connections
    tree_dict = {}
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            tree_dict[(i, j)] = (heights[i][j], set())

    # Iterate over the tree dictionary and update the connections for each tree
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            current_tree = tree_dict[(i, j)]
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if 0 <= i + di < len(heights) and 0 <= j + dj < len(heights[0]):
                        neighbor_tree = tree_dict[(i + di, j + dj)]
                        if current_tree[0] == neighbor_tree[0]:
                            current_tree[1].add((i + di, j + dj))
                            neighbor_tree[1].add((i, j))

    # Find the largest connected group of trees with the same height
    largest_group = None
    for tree in tree_dict.values():
        if largest_group is None or len(largest_group[1]) < len(tree[1]):
            largest_group = tree

    return len(largest_group[1])

