
def get_swap_pairs(n, a, p):
    # Initialize a dictionary to store the apples on each node
    apples = {i: a[i-1] for i in range(1, n+1)}
    # Initialize a list to store the parents of each node
    parents = [0] + p
    # Initialize a list to store the swap pairs
    swap_pairs = []
    
    # Loop through each node except the root
    for i in range(2, n+1):
        # If the current node is a leaf
        if parents[i] != 0:
            # Get the parent of the current node
            parent = parents[i]
            # Get the number of apples on the current node
            num_apples = apples[i]
            # Get the number of apples on the parent node
            parent_apples = apples[parent]
            # If the number of apples on the current node is equal to the number of apples on the parent node
            if num_apples == parent_apples:
                # Add the current node and its parent to the swap pairs
                swap_pairs.append((i, parent))
    
    # Return the number of swap pairs
    return len(swap_pairs)

def main():
    # Read the number of nodes and apples from stdin
    n = int(input())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    
    # Call the get_swap_pairs function and print the result
    print(get_swap_pairs(n, a, p))

if __name__ == '__main__':
    main()

