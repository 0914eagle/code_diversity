
def f1(n, edges):
    # create an empty graph with n vertices and no edges
    graph = [[] for _ in range(n)]

    # add edges to the graph
    for edge in edges:
        graph[edge[0] - 1].append(edge[1])
        graph[edge[1] - 1].append(edge[0])

    # check if the graph is connected and has no cycles
    visited = [False] * n
    queue = [0]
    while queue:
        vertex = queue.pop(0)
        if visited[vertex]:
            continue
        visited[vertex] = True
        queue += graph[vertex]

    # if the graph is connected and has no cycles, return the graph
    if all(visited):
        return graph
    else:
        return None

def f2(graph):
    # find the root of the tree
    root = 0
    for i in range(len(graph)):
        if len(graph[i]) == 1:
            root = i
            break

    # perform a depth-first search starting from the root
    visited = [False] * len(graph)
    result = []
    def dfs(vertex):
        if visited[vertex]:
            return
        visited[vertex] = True
        for neighbor in graph[vertex]:
            dfs(neighbor)
        result.append(vertex + 1)
    dfs(root)

    # return the result in the correct format
    return result

if __name__ == '__main__':
    n = int(input())
    edges = []
    for i in range(n - 1):
        a, b = map(int, input().split())
        edges.append((a, b))
    graph = f1(n, edges)
    if graph is None:
        print("NO")
    else:
        print("YES")
        result = f2(graph)
        for i in range(n - 1):
            print(result[i], result[i + 1])

