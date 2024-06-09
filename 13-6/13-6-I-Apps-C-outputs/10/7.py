
def is_k_multihedgehog(n, k, edges):
    # Initialize a dictionary to store the degree of each vertex
    degrees = {}
    for i in range(1, n+1):
        degrees[i] = 0
    
    # Count the degree of each vertex based on the given edges
    for edge in edges:
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1
    
    # Check if there is a vertex with degree at least k
    has_center = False
    for vertex, degree in degrees.items():
        if degree >= k:
            has_center = True
            break
    
    # If there is no vertex with degree at least k, return False
    if not has_center:
        return False
    
    # If there is a vertex with degree at least k, check if the graph is a tree
    return is_tree(n, edges)

def is_tree(n, edges):
    # Initialize a set to store the visited vertices
    visited = set()
    
    # Check if the graph is connected
    for edge in edges:
        if edge[0] not in visited:
            visited.add(edge[0])
        if edge[1] not in visited:
            visited.add(edge[1])
    
    # If the graph is not connected, return False
    if len(visited) != n:
        return False
    
    # If the graph is connected, check if it has no cycles
    for edge in edges:
        if edge[0] in visited and edge[1] in visited:
            return False
    
    # If the graph has no cycles, return True
    return True

n, k = map(int, input().split())
edges = []
for i in range(n-1):
    u, v = map(int, input().split())
    edges.append((u, v))

if is_k_multihedgehog(n, k, edges):
    print("Yes")
else:
    print("No")

