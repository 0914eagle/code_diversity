
def solve(n, x, edges):
    # Create a graph object from the edges
    graph = {i: set() for i in range(1, n + 1)}
    for i, j in edges:
        graph[i].add(j)
        graph[j].add(i)
    
    # Breadth-first search to find the shortest path from vertex 1 to vertex x
    queue = [1]
    visited = set()
    while queue:
        vertex = queue.pop(0)
        if vertex == x:
            return 0
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    
    # If vertex x is not reachable from vertex 1, return -1
    return -1

