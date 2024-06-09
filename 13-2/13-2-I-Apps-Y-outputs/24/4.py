
def get_maximum_weight_subset(n, k, a, edges):
    # Initialize a dictionary to store the weights of the vertices
    weights = {i: a[i - 1] for i in range(1, n + 1)}
    # Initialize a dictionary to store the distances between vertices
    distances = {}
    # Loop through the edges and calculate the distances between vertices
    for edge in edges:
        u, v = edge[0], edge[1]
        distances[(u, v)] = 1
        distances[(v, u)] = 1
    # Loop through the vertices and calculate the maximum weight subset
    max_weight = 0
    for i in range(1, n + 1):
        # Initialize a set to store the vertices in the current subset
        subset = set()
        # Initialize a queue to store the vertices to be processed
        queue = [i]
        # Loop through the queue and process each vertex
        while queue:
            # Get the current vertex from the queue
            vertex = queue.pop(0)
            # If the vertex is not in the subset, add it to the subset and update the maximum weight
            if vertex not in subset:
                subset.add(vertex)
                max_weight += weights[vertex]
                # Add the neighbors of the current vertex to the queue
                for edge in edges:
                    u, v = edge[0], edge[1]
                    if u == vertex and v not in subset and distances[(u, v)] > k:
                        queue.append(v)
                    elif v == vertex and u not in subset and distances[(v, u)] > k:
                        queue.append(u)
        # If the maximum weight is greater than the current maximum weight, return the current subset
        if max_weight > max_weight:
            return subset
    # If no subset with the maximum weight is found, return an empty set
    return set()

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    edges = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(get_maximum_weight_subset(n, k, a, edges))

if __name__ == '__main__':
    main()

