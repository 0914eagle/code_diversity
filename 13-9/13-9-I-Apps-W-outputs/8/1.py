
def get_tree_subtree_counters(tree, root, counter):
    
    # Base case: if the root vertex has no children, return
    if len(tree[root]) == 0:
        return
    
    # Recursive case: increment the counter on the root vertex and all its children
    counter[root] += 1
    for child in tree[root]:
        get_tree_subtree_counters(tree, child, counter)

def solve(n, q, edges, operations):
    
    # Initialize a dictionary to store the tree with its edges
    tree = {i: [] for i in range(1, n + 1)}
    for edge in edges:
        tree[edge[0]].append(edge[1])
    
    # Initialize a list to store the values of the counters on each vertex
    counter = [0] * (n + 1)
    
    # Perform all operations
    for operation in operations:
        get_tree_subtree_counters(tree, operation[0], counter)
    
    # Return the values of the counters on each vertex
    return counter

if __name__ == '__main__':
    n, q = map(int, input().split())
    edges = []
    for _ in range(n - 1):
        edges.append(list(map(int, input().split())))
    operations = []
    for _ in range(q):
        operations.append(list(map(int, input().split())))
    result = solve(n, q, edges, operations)
    print(*result, sep=' ')

