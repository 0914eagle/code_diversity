
def count_cycles(n, m, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    
    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # Initialize a set to store the visited nodes
    visited = set()
    
    # Initialize a counter for the number of cycles
    cycle_count = 0
    
    # Iterate through the graph
    for node in graph:
        if node not in visited:
            # If the node is not visited, start a DFS from it
            if dfs(graph, node, visited):
                # If the DFS finds a cycle, increment the cycle count
                cycle_count += 1
    
    return cycle_count

def dfs(graph, node, visited):
    # Mark the current node as visited
    visited.add(node)
    
    # Iterate through the neighbors of the current node
    for neighbor in graph[node]:
        # If the neighbor is not visited, recurse on it
        if neighbor not in visited:
            if dfs(graph, neighbor, visited):
                return True
    
    # If the current node is not the starting node, it is part of a cycle
    if node != 1:
        return True
    else:
        return False

n, m = map(int, input().split())
edges = []
for i in range(m):
    edges.append(list(map(int, input().split())))

print(count_cycles(n, m, edges))

