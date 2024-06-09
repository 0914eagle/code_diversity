
def get_maximum_weight_subset(n, k, a, edges):
    # Initialize a dictionary to store the weights of the vertices
    weights = {}
    for i in range(n):
        weights[i + 1] = a[i]
    
    # Initialize a dictionary to store the distances between the vertices
    distances = {}
    for i in range(n - 1):
        u, v = edges[i]
        distances[(u, v)] = 1
        distances[(v, u)] = 1
    
    # Initialize a set to store the vertices in the maximum weight subset
    max_weight_subset = set()
    
    # Iterate through the vertices and add them to the maximum weight subset if they are valid
    for i in range(n):
        vertex = i + 1
        if vertex not in max_weight_subset:
            # Check if the vertex is valid by checking if it has a distance more than k from any other vertex in the subset
            valid = True
            for j in range(n):
                if j + 1 in max_weight_subset and (j + 1, vertex) in distances and distances[(j + 1, vertex)] <= k:
                    valid = False
                    break
            if valid:
                max_weight_subset.add(vertex)
    
    # Return the maximum weight of the subset
    return sum(weights[vertex] for vertex in max_weight_subset)

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

