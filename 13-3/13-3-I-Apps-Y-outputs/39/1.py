
def get_most_likely_tree(samples):
    # Initialize the tree with a single node for each sample
    tree = {}
    for i, sample in enumerate(samples):
        tree[i] = [sample]

    # Iterate through the samples and find the most likely edge between them
    for i in range(len(samples)):
        for j in range(i+1, len(samples)):
            # Compute the weight of the edge between the two samples
            weight = get_edge_weight(samples[i], samples[j])

            # If the weight is less than the current minimum, update the tree
            if weight < tree[i][1] or tree[j][1]:
                tree[i] = [j, weight]
                tree[j] = [i, weight]

    # Return the tree with the smallest unlikeliness
    return tree

def get_edge_weight(s1, s2):
    # Initialize the weight to 0
    weight = 0

    # Iterate through the characters of the two strings and count the number of differences
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            weight += 1

    # Return the weight
    return weight

def main():
    # Read the input from stdin
    n, k = map(int, input().split())
    samples = [input() for _ in range(n)]

    # Get the most likely tree
    tree = get_most_likely_tree(samples)

    # Print the minimal unlikeliness of the tree
    print(min(tree.values()))

    # Print the edges of the tree
    for i in range(n):
        print(tree[i][0], i)

if __name__ == '__main__':
    main()

