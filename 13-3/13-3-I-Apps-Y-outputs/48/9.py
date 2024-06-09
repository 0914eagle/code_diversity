
def get_maximum_spanning_tree(n, m, edges):
    # Sort the edges by their weight in non-decreasing order
    edges.sort(key=lambda x: x[2])

    # Create a disjoint set data structure to store the vertices and their parents
    dsu = DisjointSetUnion(n)

    # Initialize the maximum spanning tree with the first edge
    tree = [edges[0]]

    # Iterate through the remaining edges
    for edge in edges[1:]:
        # If the edge is not part of the same connected component as the previous edge, add it to the tree
        if not dsu.find_set(edge[0]):
            tree.append(edge)
            dsu.union_set(edge[0], edge[1])

    return tree

