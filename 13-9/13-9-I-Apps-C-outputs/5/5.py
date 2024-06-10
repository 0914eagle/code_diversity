
def get_maximum_reachable_vertices(n, m, s, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[1] - 1].append(edge[2] - 1)
        if edge[0] == 2:
            graph[edge[2] - 1].append(edge[1] - 1)
    
    # Initialize a visited array and a queue
    visited = [False] * n
    queue = [s - 1]
    visited[s - 1] = True
    
    # BFS to find the maximum reachable vertices
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    
    return sum(visited)

def get_minimum_reachable_vertices(n, m, s, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[1] - 1].append(edge[2] - 1)
        if edge[0] == 2:
            graph[edge[2] - 1].append(edge[1] - 1)
    
    # Initialize a visited array and a queue
    visited = [False] * n
    queue = [s - 1]
    visited[s - 1] = True
    
    # BFS to find the minimum reachable vertices
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    
    return sum(visited)

def orient_edges(n, m, s, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[1] - 1].append(edge[2] - 1)
        if edge[0] == 2:
            graph[edge[2] - 1].append(edge[1] - 1)
    
    # Initialize a visited array and a queue
    visited = [False] * n
    queue = [s - 1]
    visited[s - 1] = True
    
    # BFS to find the minimum reachable vertices
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    
    # Initialize the output strings
    output_1 = str(sum(visited)) + '\n'
    output_2 = str(sum(visited)) + '\n'
    
    # Orient the edges
    for edge in edges:
        if edge[0] == 2:
            if visited[edge[1] - 1] and visited[edge[2] - 1]:
                output_1 += '+'
                output_2 += '-'
            elif visited[edge[1] - 1] and not visited[edge[2] - 1]:
                output_1 += '-'
                output_2 += '+'
            else:
                output_1 += '+'
                output_2 += '+'
    
    return output_1, output_2

if __name__ == '__main__':
    n, m, s = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    
    output_1, output_2 = orient_edges(n, m, s, edges)
    print(output_1)
    print(output_2)

