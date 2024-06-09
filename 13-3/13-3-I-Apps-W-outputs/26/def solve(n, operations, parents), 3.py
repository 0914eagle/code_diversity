
def solve(n, operations, parents):
    # Initialize the tree with the given operations and parents
    tree = [0] * (n + 1)
    tree[0] = 0
    for i in range(1, n):
        tree[i] = operations[i - 1]
    for i in range(1, n):
        tree[parents[i - 1]] = parents[i - 1]
    
    # Initialize the numbers to be placed in the leaves
    numbers = [i for i in range(1, n + 1)]
    
    # Initialize the maximum value in the root
    max_value = 0
    
    # Place the numbers in the leaves
    for i in range(n, 0, -1):
        if tree[i] == 0:
            # Node i is a leaf, place the next number in it
            tree[i] = numbers.pop()
        else:
            # Node i is not a leaf, find the maximum or minimum value in its sons
            son1 = tree[i]
            son2 = tree[son1]
            if tree[i] == 1:
                # Node i has operation max, find the maximum value in its sons
                tree[i] = max(tree[son1], tree[son2])
            else:
                # Node i has operation min, find the minimum value in its sons
                tree[i] = min(tree[son1], tree[son2])
    
    # Find the maximum value in the root
    max_value = tree[1]
    
    return max_value

