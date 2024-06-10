
def read_input():
    n, m = map(int, input().split())
    corridors = []
    for _ in range(m):
        u, v = map(int, input().split())
        corridors.append((u, v))
    return n, m, corridors

def remove_corridors(n, m, corridors):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for u, v in corridors:
        graph[u-1].append(v-1)
    
    # Find all connected components in the graph
    connected_components = []
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            component = []
            dfs(graph, i, visited, component)
            connected_components.append(component)
    
    # Remove all corridors that connect two connected components
    removed_corridors = []
    for u, v in corridors:
        if connected_components[u-1] is not connected_components[v-1]:
            removed_corridors.append((u, v))
    
    return len(removed_corridors) // 2, removed_corridors

def dfs(graph, start, visited, component):
    visited[start] = True
    component.append(start)
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, component)

if __name__ == '__main__':
    n, m, corridors = read_input()
    removed_corridors = remove_corridors(n, m, corridors)
    print(removed_corridors[0])
    for corridor in removed_corridors[1]:
        print(corridor[0], corridor[1])

