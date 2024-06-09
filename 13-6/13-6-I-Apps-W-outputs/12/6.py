
import sys

def shortest_paths(graph, start, end):
    # Initialize the distance from start to start as 0
    distance = {start: 0}
    # Initialize the predecessor of start to None
    predecessor = {start: None}
    # Initialize the queue with the start vertex
    queue = [start]

    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.pop(0)
        # Get all the neighbors of the dequeued vertex
        neighbors = graph[vertex]
        # Iterate through all the neighbors
        for neighbor in neighbors:
            # If the neighbor has not been visited yet, visit it and update the distance and the predecessor
            if neighbor not in distance:
                distance[neighbor] = distance[vertex] + 1
                predecessor[neighbor] = vertex
                queue.append(neighbor)
            # If the neighbor has been visited and the distance through the current vertex is less than the already known distance, update the distance and the predecessor
            elif distance[neighbor] > distance[vertex] + 1:
                distance[neighbor] = distance[vertex] + 1
                predecessor[neighbor] = vertex

    # Return the distance of the end vertex from the start vertex
    return distance[end]

def find_shortest_paths(graph, start, end):
    # Initialize the number of shortest paths as 0
    num_shortest_paths = 0
    # Initialize the queue with the start vertex
    queue = [start]

    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.pop(0)
        # If the vertex is the end vertex, increment the number of shortest paths
        if vertex == end:
            num_shortest_paths += 1
        # Get all the neighbors of the dequeued vertex
        neighbors = graph[vertex]
        # Iterate through all the neighbors
        for neighbor in neighbors:
            # If the neighbor has not been visited yet, visit it and add it to the queue
            if neighbor not in graph:
                queue.append(neighbor)

    # Return the number of shortest paths
    return num_shortest_paths

def main():
    # Read the number of vertices and edges from stdin
    num_vertices, num_edges = map(int, input().split())
    # Read the edges from stdin
    graph = {}
    for _ in range(num_edges):
        u, v, w = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, w))
        graph[v].append((u, w))
    # Read the start and end vertices from stdin
    start, end = map(int, input().split())
    # Find the shortest path between the start and end vertices
    distance = shortest_paths(graph, start, end)
    # Find the number of shortest paths between the start and end vertices
    num_shortest_paths = find_shortest_paths(graph, start, end)
    # Print the number of shortest paths
    print(num_shortest_paths)

if __name__ == '__main__':
    main()

