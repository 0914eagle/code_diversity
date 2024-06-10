
def get_swap_count(n, a, p):
    # Initialize the count of swaps to 0
    swap_count = 0
    
    # Loop through each node except the root
    for i in range(2, n+1):
        # If the node has at least one apple
        if a[i-1] > 0:
            # Find the parent of the node
            parent = p[i-1]
            
            # If the parent has at least one apple
            if a[parent-1] > 0:
                # Increment the count of swaps
                swap_count += 1
    
    # Return the count of swaps
    return swap_count

def get_apples_after_swap(n, a, p, u, v):
    # Create a copy of the apples array
    a_copy = a.copy()
    
    # Swap the apples of nodes u and v
    a_copy[u-1], a_copy[v-1] = a_copy[v-1], a_copy[u-1]
    
    # Return the copy of the apples array
    return a_copy

def get_winning_move(n, a, p, u, v):
    # Get the apples after the swap
    a_after_swap = get_apples_after_swap(n, a, p, u, v)
    
    # Initialize the count of apples on leaves to 0
    leaf_count = 0
    
    # Loop through each node except the root
    for i in range(2, n+1):
        # If the node is a leaf
        if p[i-1] == i:
            # Increment the count of apples on leaves
            leaf_count += a_after_swap[i-1]
    
    # If the count of apples on leaves is even
    if leaf_count % 2 == 0:
        # Return "NO"
        return "NO"
    else:
        # Return "YES"
        return "YES"

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    u, v = map(int, input().split())
    print(get_winning_move(n, a, p, u, v))

