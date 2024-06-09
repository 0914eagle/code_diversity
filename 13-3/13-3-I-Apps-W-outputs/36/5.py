
def find_centroid(n, edges):
    # Initialize a dictionary to store the degree of each vertex
    degrees = {}
    for i in range(1, n+1):
        degrees[i] = 0
    
    # Calculate the degree of each vertex by counting the number of edges incident to it
    for edge in edges:
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1
    
    # Find the vertex with the smallest degree
    min_degree = min(degrees.values())
    centroids = [vertex for vertex, degree in degrees.items() if degree == min_degree]
    
    return centroids[0]

def add_edge(n, edges, x, y):
    edges.append([x, y])
    return edges

def cut_edge(n, edges, x, y):
    edges.remove([x, y])
    return edges

def f1(n, edges):
    centroid = find_centroid(n, edges)
    return centroid, centroid

def f2(n, edges):
    centroid = find_centroid(n, edges)
    neighbors = [edge[1] for edge in edges if edge[0] == centroid]
    for neighbor in neighbors:
        edges = cut_edge(n, edges, centroid, neighbor)
        edges = add_edge(n, edges, centroid, neighbor)
        centroid = find_centroid(n, edges)
        if centroid != neighbors[0]:
            return centroid, neighbors[0]
    return centroid, neighbors[0]

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = []
        for _ in range(n-1):
            x, y = map(int, input().split())
            edges.append([x, y])
        print(f1(n, edges))
        print(f2(n, edges))

