
def solve(n, parent, x):
    # Check if the input is valid
    if len(parent) != n or len(x) != n:
        return "IMPOSSIBLE"
    
    # Initialize the tree with the root node
    tree = {1: {}}
    
    # Add the other nodes to the tree
    for i in range(2, n+1):
        tree[i] = {parent[i-1]}
    
    # Check if the tree is a binary tree
    if len(tree[1]) != 2:
        return "IMPOSSIBLE"
    
    # Initialize the color and weight of the root node
    color = 0
    weight = x[1]
    
    # Recursively allocate colors and weights to the nodes
    allocate_colors(tree, 1, color, weight, x)
    
    # Check if the condition is satisfied for all nodes
    for i in range(1, n+1):
        if weight != x[i]:
            return "IMPOSSIBLE"
    
    return "POSSIBLE"

def allocate_colors(tree, node, color, weight, x):
    # Base case: if the node has no children, return
    if not tree[node]:
        return
    
    # Recursive case: allocate colors and weights to the children
    for child in tree[node]:
        allocate_colors(tree, child, 1-color, weight-x[child], x)

if __name__ == '__main__':
    n = int(input())
    parent = list(map(int, input().split()))
    x = list(map(int, input().split()))
    print(solve(n, parent, x))

