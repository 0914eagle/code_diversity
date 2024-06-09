
def get_min_unlikeliness_tree(samples):
    # Initialize the tree with a single node for each sample
    tree = {}
    for i, sample in enumerate(samples):
        tree[i] = {i}

    # Iterate through the samples and add edges between the nodes
    for i in range(len(samples)):
        for j in range(i+1, len(samples)):
            # Get the number of positions at which the two strings differ
            diff = 0
            for k in range(len(samples[0])):
                if samples[i][k] != samples[j][k]:
                    diff += 1
            # Add an edge between the nodes with weight equal to the number of differences
            tree[i].add(j)
            tree[j].add(i)
            tree[i][j] = diff
            tree[j][i] = diff

    # Find the minimum unlikeliness tree by starting with the tree with the smallest number of edges
    # and iteratively adding edges between nodes until no more edges can be added
    min_unlikeliness = float('inf')
    for i in range(1, len(samples)):
        for j in range(i+1, len(samples)):
            if tree[i][j] < min_unlikeliness:
                min_unlikeliness = tree[i][j]
                min_tree = (i, j)

    return min_unlikeliness, min_tree

