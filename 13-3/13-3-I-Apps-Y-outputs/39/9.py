
def get_minimal_unlikeliness_tree(samples):
    # Initialize the tree with a single node for each sample
    tree = {i: [i] for i in range(len(samples))}
    # Iterate through the samples and find the most likely edge between them
    for i in range(len(samples)):
        for j in range(i+1, len(samples)):
            # Compute the weight of the edge between the two samples
            weight = len(set(samples[i]) ^ set(samples[j]))
            # If the weight is less than the current minimum, update the tree
            if weight < tree[i][1]:
                tree[i] = [j, weight]
    # Find the root of the tree by finding the sample with no parent
    root = next((i for i in range(len(samples)) if not any(i in tree[j] for j in range(len(samples)) if i != j)), None)
    # Traverse the tree and print the edges
    edges = []
    for i in range(len(samples)):
        if i != root:
            edges.append([root, i])
            root = tree[root][0]
    return tree[0][1], edges

