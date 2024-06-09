
def get_maximum_weight_subset(n, k, a, edges):
    # Initialize a dictionary to store the weights of the vertices
    weights = {}
    for i in range(n):
        weights[i + 1] = a[i]
    
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {}
    for edge in edges:
        u, v = edge
        if u not in neighbors:
            neighbors[u] = []
        neighbors[u].append(v)
        if v not in neighbors:
            neighbors[v] = []
        neighbors[v].append(u)
    
    # Initialize a set to store the vertices that are at a distance more than k from each other
    visited = set()
    
    # Initialize a queue to perform a BFS traversal of the graph
    queue = [1]
    
    # Perform a BFS traversal of the graph starting from vertex 1
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in neighbors[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    # Initialize a set to store the vertices that are at a distance more than k from each other
    subset = set()
    
    # Add the vertices that are at a distance more than k from each other to the subset
    for vertex in visited:
        subset.add(vertex)
    
    # Initialize a variable to store the maximum total weight of the subset
    maximum_weight = 0
    
    # Iterate over the vertices in the subset and calculate the total weight of the subset
    for vertex in subset:
        maximum_weight += weights[vertex]
    
    return maximum_weight

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    edges = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(get_maximum_weight_subset(n, k, a, edges))

