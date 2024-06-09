
import sys

def shortest_paths(graph, s, t):
    # Initialize the distance of all vertices as infinite and the previous vertex of all vertices as None
    dist = {vertex: float('inf') for vertex in graph}
    prev = {vertex: None for vertex in graph}
    
    # Set the distance of the source vertex to 0 and its previous vertex to None
    dist[s] = 0
    prev[s] = None
    
    # Loop through all vertices in the graph
    for vertex in graph:
        # If the distance of the current vertex is infinite, skip it
        if dist[vertex] == float('inf'):
            continue
        
        # Loop through all neighbors of the current vertex
        for neighbor in graph[vertex]:
            # If the distance of the neighbor is greater than the distance of the current vertex plus the weight of the edge, update the distance and previous vertex
            if dist[neighbor] > dist[vertex] + graph[vertex][neighbor]:
                dist[neighbor] = dist[vertex] + graph[vertex][neighbor]
                prev[neighbor] = vertex
    
    # Return the distance of the destination vertex
    return dist[t]

def shortest_paths_with_random_params(graph, s, t):
    # Generate a random source and destination vertex
    s = random.randint(0, len(graph) - 1)
    t = random.randint(0, len(graph) - 1)
    
    # Call the shortest paths function with the random source and destination vertex
    return shortest_paths(graph, s, t)

def main():
    # Read the number of vertices and edges from stdin
    num_vertices, num_edges = map(int, input().split())
    
    # Initialize the graph as a dictionary of dictionaries
    graph = {i: {} for i in range(num_vertices)}
    
    # Read the edges from stdin
    for _ in range(num_edges):
        u, v, w = map(int, input().split())
        graph[u][v] = w
    
    # Read the source and destination vertices from stdin
    s, t = map(int, input().split())
    
    # Call the shortest paths with random params function with the graph, source, and destination vertices
    print(shortest_paths_with_random_params(graph, s, t))

if __name__ == '__main__':
    main()

