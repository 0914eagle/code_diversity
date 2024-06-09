
def find_cycles(n, m, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    
    # Add edges to the graph
    for edge in edges:
        u, v = edge[0], edge[1]
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize a set to store the visited nodes
    visited = set()
    
    # Initialize a counter for the number of cycles
    num_cycles = 0
    
    # Iterate over the graph
    for node in graph:
        if node not in visited:
            # If the node is not visited, start a DFS from it
            if dfs(graph, node, visited):
                num_cycles += 1
    
    return num_cycles

def dfs(graph, node, visited):
    # Mark the current node as visited
    visited.add(node)
    
    # If the node has no neighbors, it is a cycle
    if not graph[node]:
        return True
    
    # Recursively call DFS for all the neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(graph, neighbor, visited):
                return True
    
    return False

n, m = map(int, input().split())
edges = []
for i in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    
print(find_cycles(n, m, edges))

