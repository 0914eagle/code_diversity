
def get_most_likely_tree(samples):
    # Initialize the tree with a single node for each sample
    tree = {}
    for i, sample in enumerate(samples):
        tree[i] = [sample]

    # Iterate through the samples and add edges between the nodes
    # based on the differences between the samples
    for i in range(len(samples)):
        for j in range(i+1, len(samples)):
            diff = 0
            for k in range(len(samples[0])):
                if samples[i][k] != samples[j][k]:
                    diff += 1
            tree[i].append(j)
            tree[j].append(i)

    # Return the tree with the smallest unlikeliness
    return tree

