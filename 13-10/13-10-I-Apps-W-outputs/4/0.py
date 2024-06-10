
def get_swap_count(nodes, apples, parents):
    # Initialize a dictionary to store the number of apples on each node
    node_apples = {i: apples[i-1] for i in range(1, len(apples)+1)}
    
    # Initialize a set to store the nodes that are leaves
    leaves = set()
    
    # Find all leaves in the tree
    for i in range(1, len(apples)+1):
        if node_apples[i] != 0:
            leaves.add(i)
    
    # Initialize a set to store the pairs of nodes that can be swapped
    swaps = set()
    
    # Iterate over all possible pairs of nodes
    for i in range(1, len(apples)+1):
        for j in range(i+1, len(apples)+1):
            # Check if the nodes are not already leaves
            if i not in leaves and j not in leaves:
                # Check if the nodes have different number of apples
                if node_apples[i] != node_apples[j]:
                    # Add the pair of nodes to the set of swaps
                    swaps.add((i, j))
    
    # Return the number of swaps
    return len(swaps)

def main():
    # Read the number of nodes and apples from stdin
    nodes = int(input())
    apples = [int(i) for i in input().split()]
    parents = [int(i) for i in input().split()]
    
    # Call the get_swap_count function and print the result
    print(get_swap_count(nodes, apples, parents))

if __name__ == '__main__':
    main()

