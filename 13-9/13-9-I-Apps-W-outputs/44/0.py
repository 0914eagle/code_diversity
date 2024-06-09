
def get_labels(n, m, edges):
    # Initialize a list to store the labels
    labels = [0] * n
    # Initialize a set to keep track of the visited vertices
    visited = set()
    # Start from the first vertex and perform DFS traversal
    dfs(edges, 1, visited, labels)
    # Return the labels list
    return labels

def dfs(edges, vertex, visited, labels):
    # Mark the current vertex as visited
    visited.add(vertex)
    # If the vertex has not been labeled, label it with the next available label
    if labels[vertex-1] == 0:
        labels[vertex-1] = len(visited)
    # Recursively visit the neighbors of the current vertex
    for neighbor in edges[vertex]:
        if neighbor not in visited:
            dfs(edges, neighbor, visited, labels)
    # Mark the current vertex as visited
    visited.add(vertex)

edges = {}
for _ in range(m):
    v, u = map(int, input().split())
    if v not in edges:
        edges[v] = [u]
    else:
        edges[v].append(u)
labels = get_labels(n, m, edges)
print(*labels)

