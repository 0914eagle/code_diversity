
def solve(n, m, n1, n2, n3, edges):
    # Initialize a dictionary to store the number of vertices with each label
    label_count = {1: n1, 2: n2, 3: n3}
    # Initialize a set to store the edges
    edge_set = set(edges)
    # Iterate through the edges and update the label count
    for u, v in edge_set:
        for label in [1, 2, 3]:
            if label_count[label] > 0:
                label_count[label] -= 1
                break
        else:
            return "NO"
    # Check if all vertices have been labeled
    if sum(label_count.values()) > 0:
        return "NO"
    # Return the labeling
    return "YES\n" + "".join(str(label) for label in label_count)

