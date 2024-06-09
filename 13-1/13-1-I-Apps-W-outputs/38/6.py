
def f1(n, a):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the input
    for i in range(n):
        graph[i].append(a[i] - 1)

    # Count the number of strongly connected components in the graph
    return strongly_connected_components(graph)

def f2(n, a):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the input
    for i in range(n):
        graph[i].append(a[i] - 1)

    # Count the number of strongly connected components in the graph
    return strongly_connected_components(graph)

def strongly_connected_components(graph):
    # Initialize a visited array and a component array
    visited = [False] * len(graph)
    component = [0] * len(graph)

    # Iterate through all nodes in the graph
    for node in range(len(graph)):
        # If the node has not been visited, perform a DFS traversal
        if not visited[node]:
            dfs(graph, visited, component, node)

    # Return the number of strongly connected components
    return len(set(component))

def dfs(graph, visited, component, node):
    # Mark the current node as visited
    visited[node] = True

    # Iterate through all neighbors of the current node
    for neighbor in graph[node]:
        # If the neighbor has not been visited, perform a DFS traversal
        if not visited[neighbor]:
            dfs(graph, visited, component, neighbor)

    # Add the current node to the component array
    component[node] = 1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))
    print(f2(n, a))

