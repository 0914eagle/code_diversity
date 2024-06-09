
def find_centroid(n, edges):
    # Initialize a dictionary to store the degree of each vertex
    degrees = {}
    for i in range(1, n+1):
        degrees[i] = 0
    
    # Calculate the degree of each vertex by counting the number of edges incident to it
    for edge in edges:
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1
    
    # Find the vertex with the smallest degree, which is the centroid
    centroid = 1
    for i in range(2, n+1):
        if degrees[i] < degrees[centroid]:
            centroid = i
    
    return centroid

def find_edge_to_cut(n, edges, centroid):
    # Find an edge that is not incident to the centroid
    for edge in edges:
        if edge[0] != centroid and edge[1] != centroid:
            return edge
    
    # If all edges are incident to the centroid, return an arbitrary edge
    return edges[0]

def find_edge_to_add(n, edges, centroid):
    # Find an edge that is not incident to the centroid
    for edge in edges:
        if edge[0] != centroid and edge[1] != centroid:
            return edge
    
    # If all edges are incident to the centroid, return an arbitrary edge
    return edges[0]

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = []
        for _ in range(n-1):
            x, y = map(int, input().split())
            edges.append((x, y))
        
        centroid = find_centroid(n, edges)
        edge_to_cut = find_edge_to_cut(n, edges, centroid)
        edge_to_add = find_edge_to_add(n, edges, centroid)
        
        print(edge_to_cut[0], edge_to_cut[1])
        print(edge_to_add[0], edge_to_add[1])

if __name__ == '__main__':
    main()

