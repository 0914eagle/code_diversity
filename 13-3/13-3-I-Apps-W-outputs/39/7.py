
def count_valid_pairs(n, edges):
    # Initialize a dictionary to store the edges and their corresponding numbers
    edge_nums = {}
    for edge in edges:
        edge_nums[tuple(edge[:2])] = edge[2]

    # Initialize a set to store the valid pairs
    valid_pairs = set()

    # Iterate over the edges and check if they are valid
    for i in range(n - 1):
        for j in range(i + 1, n):
            edge1 = tuple(sorted([i, j]))
            edge2 = tuple(sorted([j, i]))
            if edge1 in edge_nums and edge2 in edge_nums:
                if edge_nums[edge1] == 1 and edge_nums[edge2] == 0:
                    valid_pairs.add(edge1)

    return len(valid_pairs)

