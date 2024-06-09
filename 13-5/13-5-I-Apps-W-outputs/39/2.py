
def f1(n, roads):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for i in range(n):
        graph[i].append(roads[i] - 1)

    # Find all strongly connected components in the graph
    strongly_connected_components = []
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            strongly_connected_components.append(dfs(graph, visited, i))

    # Count the number of strongly connected components that have more than 1 node
    count = 0
    for component in strongly_connected_components:
        if len(component) > 1:
            count += 1

    return count

def dfs(graph, visited, node):
    visited[node] = True
    component = [node]
    for neighbor in graph[node]:
        if not visited[neighbor]:
            component += dfs(graph, visited, neighbor)
    return component

def f2(n, roads):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for i in range(n):
        graph[i].append(roads[i] - 1)

    # Find all strongly connected components in the graph
    strongly_connected_components = []
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            strongly_connected_components.append(dfs(graph, visited, i))

    # Count the number of strongly connected components that have more than 1 node
    count = 0
    for component in strongly_connected_components:
        if len(component) > 1:
            count += 1

    return count

if __name__ == '__main__':
    n = int(input())
    roads = list(map(int, input().split()))
    print(f1(n, roads))
    print(f2(n, roads))

