
def get_min_unlikeliness_tree(samples):
    # Initialize the unlikeliness of the tree as infinity
    unlikeliness = float('inf')
    # Initialize the optimal tree as an empty dictionary
    optimal_tree = {}

    # Iterate over all possible trees
    for tree in itertools.product('ATGC', repeat=len(samples)):
        # Convert the tree to a dictionary with the samples as keys and the parents as values
        tree_dict = {i: tree[i] for i in range(len(samples))}
        # Get the unlikeliness of the current tree
        current_unlikeliness = get_unlikeliness(tree_dict, samples)
        # If the current tree has a lower unlikeliness than the current optimal tree, update the optimal tree
        if current_unlikeliness < unlikeliness:
            unlikeliness = current_unlikeliness
            optimal_tree = tree_dict

    # Return the optimal tree and its unlikeliness
    return optimal_tree, unlikeliness

def get_unlikeliness(tree, samples):
    # Initialize the unlikeliness as zero
    unlikeliness = 0
    # Iterate over all samples
    for i in range(len(samples)):
        # If the sample has a parent, add the number of positions at which the sample and its parent differ to the unlikeliness
        if tree[i] != '-':
            unlikeliness += get_difference_count(samples[i], samples[tree[i]])
    # Return the unlikeliness
    return unlikeliness

def get_difference_count(str1, str2):
    # Initialize the difference count as zero
    difference_count = 0
    # Iterate over all positions in the strings
    for i in range(len(str1)):
        # If the characters at the current position are different, increment the difference count
        if str1[i] != str2[i]:
            difference_count += 1
    # Return the difference count
    return difference_count

def main():
    # Read the number of samples and the length of each sample from stdin
    n, k = map(int, input().split())
    # Read the samples from stdin
    samples = [input() for _ in range(n)]
    # Get the optimal tree and its unlikeliness
    optimal_tree, unlikeliness = get_min_unlikeliness_tree(samples)
    # Print the unlikeliness of the optimal tree
    print(unlikeliness)
    # Print the edges of the optimal tree
    for i in range(n):
        if optimal_tree[i] != '-':
            print(i, optimal_tree[i])

if __name__ == '__main__':
    main()

