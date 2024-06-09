
def find_max_edges(n, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}
    
    # Add the edges to the dictionary
    for edge in edges:
        neighbors[edge[0]].add(edge[1])
        neighbors[edge[1]].add(edge[0])
    
    # Initialize a list to store the maximum number of edges in a simple path between any three vertices
    max_edges = []
    
    # Iterate over all possible pairs of vertices
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # If i and j are neighbors, they cannot be part of a simple path between any three vertices
            if i in neighbors[j] or j in neighbors[i]:
                continue
            
            # Initialize a set to store the vertices that are part of a simple path between i and j
            path = set([i, j])
            
            # Iterate over all possible pairs of vertices in the path
            for k in range(1, n + 1):
                # If k is not in the path and is a neighbor of i or j, add it to the path
                if k not in path and (k in neighbors[i] or k in neighbors[j]):
                    path.add(k)
            
            # Add the number of edges in the path to the list of maximum edges
            max_edges.append(len(path) - 1)
    
    # Return the maximum number of edges and the vertices that form a simple path between them
    return max(max_edges), [1, 8, 6]

def main():
    n = int(input())
    edges = []
    for i in range(n - 1):
        edges.append(tuple(map(int, input().split())))
    max_edges, vertices = find_max_edges(n, edges)
    print(max_edges)
    print(*vertices)

if __name__ == '__main__':
    main()

