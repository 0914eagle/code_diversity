
def is_acyclic(n, m, edges):
    # Initialize a dictionary to keep track of the vertices and their neighbors
    neighbors = {i: set() for i in range(1, n + 1)}
    for u, v in edges:
        neighbors[u].add(v)
    
    # Initialize a set to keep track of the visited vertices
    visited = set()
    
    # Iterate through the vertices and check if there is a cycle
    for vertex in neighbors:
        if vertex not in visited:
            if not dfs(vertex, neighbors, visited):
                return False
    
    return True

def dfs(vertex, neighbors, visited):
    # Mark the current vertex as visited
    visited.add(vertex)
    
    # Recursively explore the neighbors of the current vertex
    for neighbor in neighbors[vertex]:
        if neighbor not in visited:
            if not dfs(neighbor, neighbors, visited):
                return False
    
    return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print("YES" if is_acyclic(n, m, edges) else "NO")

