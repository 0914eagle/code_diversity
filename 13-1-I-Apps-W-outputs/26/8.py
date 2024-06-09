
def solve(n, x, edges):
    # Create a graph object from the edges
    graph = {i: set() for i in range(1, n + 1)}
    for i, j in edges:
        graph[i].add(j)
        graph[j].add(i)
    
    # Find the shortest path from vertex 1 to vertex x
    visited = set()
    queue = [(1, [])]
    while queue:
        vertex, path = queue.pop(0)
        if vertex == x:
            return len(path)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    # If there is no path from vertex 1 to vertex x, return -1
    return -1

