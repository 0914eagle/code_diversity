
def f1(n, edges):
    # create a graph object
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # find the maximum number of edges in a simple path between any two vertices
    max_edges = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                path = []
                dfs(graph, i, j, path)
                max_edges = max(max_edges, len(path))
    
    return max_edges

def f2(n, edges):
    # create a graph object
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # find the maximum number of edges in a simple path between any two vertices
    max_edges = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                path = []
                dfs(graph, i, j, path)
                max_edges = max(max_edges, len(path))
    
    # find the vertices that form the maximum number of edges in a simple path
    max_vertices = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                path = []
                dfs(graph, i, j, path)
                if len(path) == max_edges:
                    max_vertices.append(i)
                    max_vertices.append(j)
    
    return list(set(max_vertices))

def dfs(graph, start, end, path):
    if start == end:
        path.append(start)
        return
    for neighbor in graph[start]:
        if neighbor not in path:
            path.append(start)
            dfs(graph, neighbor, end, path)

if __name__ == '__main__':
    n = int(input())
    edges = []
    for i in range(n-1):
        edges.append(list(map(int, input().split())))
    print(f1(n, edges))
    print(*f2(n, edges))

