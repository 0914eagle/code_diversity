
def solve(n, operations, parents):
    # Initialize the tree with the given operations and parents
    tree = [0] * (n + 1)
    for i in range(1, n + 1):
        tree[i] = {"operation": operations[i - 1], "parent": parents[i - 1]}
    
    # Initialize the numbers to be placed in the leaves
    numbers = [i for i in range(1, n + 1)]
    
    # Initialize the maximum number in the root to be 0
    max_root = 0
    
    # Loop through the leaves and place the numbers accordingly
    for i in range(n, 0, -1):
        if tree[i]["operation"] == 0:
            # If the current node is a leaf with minimum operation, place the smallest number
            tree[i]["number"] = min(numbers)
            numbers.remove(tree[i]["number"])
        else:
            # If the current node is a leaf with maximum operation, place the largest number
            tree[i]["number"] = max(numbers)
            numbers.remove(tree[i]["number"])
        
        # Update the maximum number in the root
        max_root = max(max_root, tree[i]["number"])
    
    return max_root

