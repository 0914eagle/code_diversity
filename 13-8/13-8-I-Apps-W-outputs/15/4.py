
def get_relatively_prime_graph(n, m):
    # Initialize an empty graph with n vertices and m edges
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Iterate through all possible edges
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # If the current edge is valid, add it to the graph
            if gcd(i, j) == 1:
                graph[i][j] = 1
                graph[j][i] = 1
    
    # Check if the graph is connected
    if not is_connected(graph):
        return "Impossible"
    
    # Check if the graph contains self-loops or multiple edges
    if contains_self_loops(graph) or contains_multiple_edges(graph):
        return "Impossible"
    
    # If the graph is valid, return it
    return "Possible\n" + "\n".join(str(edge) for edge in get_edges(graph))

def is_connected(graph):
    # Initialize a visited array and a queue
    visited = [False] * (len(graph) + 1)
    queue = [1]
    
    # Mark the first vertex as visited and enqueue it
    visited[1] = True
    
    # Iterate through the queue
    while queue:
        # Dequeue a vertex
        vertex = queue.pop(0)
        
        # Iterate through the neighbors of the dequeued vertex
        for neighbor in range(1, len(graph) + 1):
            # If the neighbor is not visited, mark it as visited and enqueue it
            if graph[vertex][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    # If all vertices are visited, the graph is connected
    return all(visited)

def contains_self_loops(graph):
    # Iterate through the graph
    for vertex in range(1, len(graph) + 1):
        # If the vertex has a self-loop, return True
        if graph[vertex][vertex] == 1:
            return True
    
    # If no vertex has a self-loop, return False
    return False

def contains_multiple_edges(graph):
    # Iterate through the graph
    for vertex in range(1, len(graph) + 1):
        # Iterate through the neighbors of the current vertex
        for neighbor in range(1, len(graph) + 1):
            # If the current vertex has more than one edge with the neighbor, return True
            if graph[vertex][neighbor] > 1:
                return True
    
    # If no vertex has more than one edge with any neighbor, return False
    return False

def get_edges(graph):
    # Initialize an empty list to store the edges
    edges = []
    
    # Iterate through the graph
    for vertex in range(1, len(graph) + 1):
        # Iterate through the neighbors of the current vertex
        for neighbor in range(1, len(graph) + 1):
            # If the current vertex has an edge with the neighbor, add it to the list of edges
            if graph[vertex][neighbor] == 1:
                edges.append((vertex, neighbor))
    
    # Return the list of edges
    return edges

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_relatively_prime_graph(n, m))

