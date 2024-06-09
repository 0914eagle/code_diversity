
def get_maximum_weight_subset(n, k, a, edges):
    # Initialize a dictionary to store the weights of the vertices
    weights = {i: a[i - 1] for i in range(1, n + 1)}
    # Initialize a dictionary to store the distances between the vertices
    distances = {}
    # Loop through the edges and calculate the distances between the vertices
    for edge in edges:
        u, v = edge[0], edge[1]
        distances[(u, v)] = 1
        distances[(v, u)] = 1
    # Loop through the vertices and calculate the maximum weight subset
    max_weight = 0
    for i in range(1, n + 1):
        # Initialize a set to store the vertices in the current subset
        current_subset = set()
        # Initialize a queue to store the vertices to be processed
        queue = [i]
        # Loop through the queue and process each vertex
        while queue:
            # Get the current vertex from the queue
            vertex = queue.pop(0)
            # If the vertex is not in the current subset, add it to the current subset
            if vertex not in current_subset:
                current_subset.add(vertex)
                # If the vertex has a distance less than or equal to k from any other vertex in the current subset, break the loop
                for v in current_subset:
                    if distances[(vertex, v)] <= k:
                        break
                else:
                    # If the vertex has a distance greater than k from all vertices in the current subset, add its neighbors to the queue
                    for neighbor in edges:
                        if neighbor[0] == vertex:
                            queue.append(neighbor[1])
        # If the current subset has a maximum weight, update the maximum weight
        if len(current_subset) > max_weight:
            max_weight = len(current_subset)
    return max_weight

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

