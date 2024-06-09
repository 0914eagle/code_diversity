
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
        # If the vertex is not in the maximum weight subset yet
        if vertex not in max_weight_subset:
            # Add the vertex to the maximum weight subset
            max_weight_subset.add(vertex)
            # Update the maximum total weight
            max_total_weight += weights[vertex]
            # Iterate through the neighbors of the vertex
            for neighbor in neighbors[vertex]:
                # If the neighbor is not in the maximum weight subset yet and has a distance more than k from the vertex
                if neighbor not in max_weight_subset and len(max_weight_subset) - len(neighbors[neighbor] & max_weight_subset) > k:
                    # Add the neighbor to the maximum weight subset
                    max_weight_subset.add(neighbor)
                    # Update the maximum total weight
                    max_total_weight += weights[neighbor]
    # Return the maximum total weight
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

