
def is_acyclic(graph):
    # Initialize a set to store the visited vertices
    visited = set()
    # Initialize a queue to store the vertices to be visited
    queue = [0]
    # Loop until the queue is empty
    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.pop(0)
        # If the vertex has not been visited, mark it as visited and add its neighbors to the queue
        if vertex not in visited:
            visited.add(vertex)
            queue += graph[vertex]
    # If all vertices have been visited, the graph is acyclic
    return len(visited) == len(graph)

def solve(n, m, edges):
    # Create a dictionary to store the graph
    graph = {i: [] for i in range(1, n + 1)}
    # Add the edges to the graph
    for edge in edges:
        u, v = edge
        graph[u].append(v)
    # Check if the graph is acyclic
    if is_acyclic(graph):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(solve(n, m, edges))

