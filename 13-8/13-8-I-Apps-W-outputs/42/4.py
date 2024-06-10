
def get_number_of_ways_to_win(n, a, p):
    # Initialize a dictionary to store the number of apples at each node
    apples = {i: a[i-1] for i in range(1, n+1)}
    # Initialize a list to store the children of each node
    children = {i: [] for i in range(1, n+1)}
    # Build the tree based on the parent-child relationships
    for i in range(2, n+1):
        children[p[i-1]].append(i)
    # Initialize a set to store the pairs of nodes that can be swapped
    pairs = set()
    # Iterate over all possible pairs of nodes
    for i in range(1, n):
        for j in range(i+1, n+1):
            # Check if the two nodes have the same number of apples
            if apples[i] == apples[j]:
                # Check if the two nodes have the same number of children
                if len(children[i]) == len(children[j]):
                    # Add the pair of nodes to the set of pairs
                    pairs.add((i, j))
    # Return the number of pairs of nodes that can be swapped
    return len(pairs)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    print(get_number_of_ways_to_win(n, a, p))

if __name__ == '__main__':
    main()

