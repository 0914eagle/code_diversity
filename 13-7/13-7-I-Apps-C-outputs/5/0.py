
def get_largest_connected_group(heights, growth_speeds):
    # Initialize a dictionary to store the tree heights and their connections
    tree_dict = {}
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            tree_dict[(i, j)] = (heights[i][j], set())

    # Iterate over the trees and their connections
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            # If the tree has already been visited, skip it
            if (i, j) in tree_dict:
                continue
            # If the tree has not been visited, start a BFS to find all connected trees
            queue = [(i, j)]
            while queue:
                curr_i, curr_j = queue.pop(0)
                # If the current tree has not been visited, mark it as visited and add it to the dictionary
                if (curr_i, curr_j) not in tree_dict:
                    tree_dict[(curr_i, curr_j)] = (heights[curr_i][curr_j], set())
                # Add the current tree to the set of connected trees
                tree_dict[(i, j)][1].add((curr_i, curr_j))
                # Add the neighbors of the current tree to the queue
                for neighbor in get_neighbors(curr_i, curr_j, len(heights), len(heights[0])):
                    queue.append(neighbor)

    # Find the largest connected group of trees
    largest_group = None
    for tree in tree_dict.values():
        if largest_group is None or len(tree[1]) > len(largest_group[1]):
            largest_group = tree

    # Return the size of the largest connected group
    return len(largest_group[1])

def get_neighbors(i, j, n, m):
    neighbors = []
    if i > 0:
        neighbors.append((i-1, j))
    if i < n-1:
        neighbors.append((i+1, j))
    if j > 0:
        neighbors.append((i, j-1))
    if j < m-1:
        neighbors.append((i, j+1))
    return neighbors

