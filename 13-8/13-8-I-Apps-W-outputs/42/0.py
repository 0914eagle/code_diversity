
def get_swap_count(n, apples, parents):
    # Initialize a dictionary to store the number of apples at each node
    apples_at_node = {i: apples[i-1] for i in range(1, n+1)}
    
    # Initialize a list to store the children of each node
    children = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        children[parents[i-1]].append(i)
    
    # Initialize a set to store the pairs of nodes that can be swapped
    swap_pairs = set()
    
    # Iterate over each node and its children
    for node in range(1, n+1):
        for child in children[node]:
            # If the node and its child have different numbers of apples, they can be swapped
            if apples_at_node[node] != apples_at_node[child]:
                swap_pairs.add((node, child))
    
    # Return the number of swap pairs
    return len(swap_pairs)

def main():
    n = int(input())
    apples = list(map(int, input().split()))
    parents = list(map(int, input().split()))
    print(get_swap_count(n, apples, parents))

if __name__ == '__main__':
    main()

