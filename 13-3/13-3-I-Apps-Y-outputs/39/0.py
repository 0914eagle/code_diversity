
def get_min_unlikeliness_tree(samples):
    # Initialize the tree with a single node for each sample
    tree = {i: [i] for i in range(len(samples))}

    # Iterate through the samples and find the most likely edge between them
    for i in range(len(samples)):
        for j in range(i+1, len(samples)):
            # Compute the weight of the edge between the two samples
            weight = len(set(samples[i]) ^ set(samples[j]))

            # If the weight is less than the current minimum, update the tree
            if weight < min_weight:
                min_weight = weight
                tree[i].append(j)
                tree[j].append(i)

    # Return the tree with the minimum unlikeliness
    return tree

