
def get_centroid(n, edges):
    # Initialize a dictionary to store the degree of each vertex
    degrees = {}
    for i in range(1, n+1):
        degrees[i] = 0
    
    # Calculate the degree of each vertex by counting the number of edges incident to it
    for edge in edges:
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1
    
    # Find the vertex with the minimum degree
    min_degree = min(degrees.values())
    centroids = [vertex for vertex, degree in degrees.items() if degree == min_degree]
    
    return centroids[0]

def get_edge_to_cut(n, edges, centroid):
    # Find the edge that connects the centroid to another vertex
    for edge in edges:
        if edge[0] == centroid or edge[1] == centroid:
            return edge
    
    return None

def get_edge_to_add(n, edges, centroid):
    # Find an edge that is not incident to the centroid
    for edge in edges:
        if edge[0] != centroid and edge[1] != centroid:
            return edge
    
    return None

def solve(n, edges):
    centroid = get_centroid(n, edges)
    edge_to_cut = get_edge_to_cut(n, edges, centroid)
    edge_to_add = get_edge_to_add(n, edges, centroid)
    
    return edge_to_cut, edge_to_add

if __name__ == '__main__':
    num_cases = int(input())
    for case in range(1, num_cases+1):
        n = int(input())
        edges = []
        for i in range(n-1):
            edges.append(list(map(int, input().split())))
        
        edge_to_cut, edge_to_add = solve(n, edges)
        print(edge_to_cut[0], edge_to_cut[1])
        print(edge_to_add[0], edge_to_add[1])

