
def get_swap_pairs(n, a, p):
    # Initialize a dictionary to store the apples and children of each node
    apples = {i: a[i-1] for i in range(1, n+1)}
    children = {i: [] for i in range(1, n+1)}
    for i in range(2, n+1):
        children[p[i-1]].append(i)
    
    # Initialize a set to store the pairs of nodes that can be swapped
    swap_pairs = set()
    
    # Iterate through each node and check if it is a leaf node
    for i in range(1, n+1):
        if not children[i]:
            # If the node is a leaf node, check if it has an even number of apples
            if apples[i] % 2 == 0:
                # If the node has an even number of apples, add it to the set of swap pairs
                swap_pairs.add((i, i))
    
    # Return the number of swap pairs
    return len(swap_pairs)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    print(get_swap_pairs(n, a, p))

if __name__ == '__main__':
    main()

