
def get_maximum_weight_subset(n, k, a, edges):
    # Initialize a dictionary to store the weights of the vertices
    weights = {i: a[i - 1] for i in range(1, n + 1)}
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}
    # Add the edges to the graph
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    # Initialize a set to store the vertices in the maximum weight subset
    max_weight_subset = set()
    # Initialize a variable to store the maximum total weight
    max_total_weight = 0
    # Iterate through the vertices of the graph
    for vertex in range(1, n + 1):
        # If the vertex is not in the maximum weight subset, add it and its neighbors to the subset
        if vertex not in max_weight_subset:
            max_weight_subset.add(vertex)
            max_weight_subset.update(neighbors[vertex])
            # Update the maximum total weight
            max_total_weight = max(max_total_weight, sum(weights[vertex] for vertex in max_weight_subset))
            # If the maximum total weight is greater than or equal to k, return the maximum total weight
            if max_total_weight >= k:
                return max_total_weight
            # If the maximum total weight is less than k, remove the vertex and its neighbors from the subset
            else:
                max_weight_subset.remove(vertex)
                max_weight_subset.difference_update(neighbors[vertex])
    # If all vertices are in the maximum weight subset, return the maximum total weight
    return max_total_weight

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(get_maximum_weight_subset(n, k, a, edges))

if __name__ == '__main__':
    main()

