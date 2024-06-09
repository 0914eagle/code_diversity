
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
    
    # Iterate through the vertices and find the vertex with the maximum weight
    for i in range(n):
        # If the vertex is not in the maximum weight subset, add it and update the distances
        if i + 1 not in max_weight_subset:
            max_weight_subset.add(i + 1)
            for j in range(n):
                if j + 1 not in max_weight_subset and (i + 1, j + 1) in distances:
                    distances[(i + 1, j + 1)] += 1
    
    # Find the maximum weight subset by iterating through the vertices and finding the vertex with the maximum weight
    for i in range(n):
        # If the vertex is not in the maximum weight subset, add it and update the distances
        if i + 1 not in max_weight_subset:
            max_weight_subset.add(i + 1)
            for j in range(n):
                if j + 1 not in max_weight_subset and (i + 1, j + 1) in distances:
                    distances[(i + 1, j + 1)] += 1
    
    # Return the maximum weight subset
    return max_weight_subset

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

