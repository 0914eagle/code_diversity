
def get_swap_count(n, a, p):
    # Initialize the tree with the given apples and parents
    tree = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        tree[i] = [a[i - 1]]
    for i in range(1, n):
        tree[p[i]].append(i + 1)
    
    # Initialize the swap count
    swap_count = 0
    
    # Iterate over all possible pairs of nodes
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            # Check if swapping the apples of nodes i and j will make Sagheer win the game
            if check_swap(n, tree, i, j):
                swap_count += 1
    
    return swap_count

def check_swap(n, tree, i, j):
    # Initialize the nodes to be visited
    nodes_to_visit = [i, j]
    
    # Initialize the number of apples on each leaf
    leaf_apples = [0, 0]
    
    # Iterate over all nodes to be visited
    while nodes_to_visit:
        node = nodes_to_visit.pop()
        if node in tree[node]:
            # Node is a leaf, so add its apples to the count
            leaf_apples[node == i] += tree[node][0]
        else:
            # Node is not a leaf, so add its children to the list of nodes to be visited
            nodes_to_visit += tree[node]
    
    # Check if the number of apples on each leaf is the same
    return leaf_apples[0] == leaf_apples[1]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    print(get_swap_count(n, a, p))

