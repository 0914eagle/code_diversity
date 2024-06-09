
def f1(n, a):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the input
    for i in range(n):
        graph[i].append(a[i] - 1)

    # Count the number of strongly connected components in the graph
    visited = [False] * n
    strongly_connected_components = 0
    for i in range(n):
        if not visited[i]:
            dfs(graph, visited, i)
            strongly_connected_components += 1

    # Return the number of ways to flip the roads
    return strongly_connected_components

def f2(n, a):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the input
    for i in range(n):
        graph[i].append(a[i] - 1)

    # Count the number of strongly connected components in the graph
    visited = [False] * n
    strongly_connected_components = 0
    for i in range(n):
        if not visited[i]:
            dfs(graph, visited, i)
            strongly_connected_components += 1

    # Return the number of ways to flip the roads
    return strongly_connected_components

def dfs(graph, visited, node):
    # Mark the current node as visited
    visited[node] = True

    # Recursively explore the graph starting from the current node
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))
    print(f2(n, a))

