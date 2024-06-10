
def get_swap_nodes(n, a, p):
    # Find the root node
    root = 1
    while root in p:
        root = p[root]
    
    # Initialize the tree with the given apples
    tree = [a[i] for i in range(n)]
    
    # Initialize the number of ways to swap the apples
    num_ways = 0
    
    # Iterate over all possible pairs of nodes
    for i in range(n):
        for j in range(i+1, n):
            # Check if the nodes are not the root and have different parents
            if i != root and j != root and p[i] != p[j]:
                # Swap the apples between the nodes
                tree[i], tree[j] = tree[j], tree[i]
                
                # Check if the tree has the same parity for all paths
                if has_even_parity(tree):
                    num_ways += 1
                
                # Swap the apples back
                tree[i], tree[j] = tree[j], tree[i]
    
    return num_ways

def has_even_parity(tree):
    # Initialize the parity of the current node to 0
    parity = 0
    
    # Iterate over all nodes in the tree
    for i in range(len(tree)):
        # Check if the current node has apples
        if tree[i] > 0:
            # Update the parity of the current node
            parity = 1 - parity
        
        # Check if the current node is a leaf
        if i+1 == len(tree) or tree[i+1] == 0:
            # Return False if the parity is odd
            if parity == 1:
                return False
    
    # Return True if all nodes have even parity
    return True

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    print(get_swap_nodes(n, a, p))

if __name__ == '__main__':
    main()

