
def solve(n, operations, parents):
    # Initialize the tree with the given operations and parents
    tree = [0] * (n + 1)
    for i in range(1, n + 1):
        tree[i] = {"operation": operations[i - 1], "parent": parents[i - 1]}
    
    # Initialize the leaves with the given values
    leaves = [i for i in range(1, n + 1) if tree[i]["parent"] == 0]
    for i in leaves:
        tree[i]["value"] = i
    
    # Propagate the values from the leaves to the root
    while len(leaves) > 0:
        new_leaves = []
        for i in leaves:
            parent = tree[i]["parent"]
            if parent != 0:
                if tree[parent]["operation"] == "max":
                    tree[parent]["value"] = max(tree[parent]["value"], tree[i]["value"])
                else:
                    tree[parent]["value"] = min(tree[parent]["value"], tree[i]["value"])
                if tree[parent]["parent"] == 0:
                    new_leaves.append(parent)
        leaves = new_leaves
    
    # Return the value in the root
    return tree[1]["value"]

