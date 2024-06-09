
def solve(n, operations, parents):
    # Initialize the tree with the given operations and parents
    tree = [0] * (n + 1)
    for i in range(1, n + 1):
        tree[i] = {"operation": operations[i - 1], "parent": parents[i - 1]}
    
    # Initialize the numbers to be placed in the leaves
    numbers = [i for i in range(1, n + 1)]
    
    # Initialize the maximum number in the root to be 0
    max_root = 0
    
    # Loop through the leaves and try to place each number in each leaf
    for i in range(1, n + 1):
        if tree[i]["parent"] != 0:
            continue
        
        # Get the operation in the current leaf
        operation = tree[i]["operation"]
        
        # Get the maximum number that can be placed in the current leaf
        max_number = max(numbers) if operation == 1 else min(numbers)
        
        # Update the maximum number in the root
        max_root = max(max_root, max_number)
        
        # Remove the placed number from the list of numbers
        numbers.remove(max_number)
    
    return max_root

