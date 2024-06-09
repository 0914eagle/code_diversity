
def min_spanning_tree(n):
    # Calculate the weight of the minimum spanning tree
    weight = 0
    for i in range(n):
        for j in range(i+1, n):
            weight += i ^ j
    return weight

