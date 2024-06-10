
def get_graph(n, a):
    graph = {}
    for i in range(n):
        graph[i] = []
        for j in range(i+1, n):
            if a[i] & a[j] != 0:
                graph[i].append(j)
                graph[j].append(i)
    return graph

def has_cycle(graph):
    visited = [False] * len(graph)
    def dfs(node, parent, visited):
        if visited[node]:
            return True
        visited[node] = True
        for neighbor in graph[node]:
            if neighbor != parent and dfs(neighbor, node, visited):
                return True
        return False
    for node in range(len(graph)):
        if dfs(node, -1, visited):
            return True
    return False

def get_shortest_cycle(graph):
    visited = [False] * len(graph)
    def dfs(node, parent, visited, cycle):
        if visited[node]:
            return
        visited[node] = True
        for neighbor in graph[node]:
            if neighbor != parent and dfs(neighbor, node, visited, cycle):
                return
        cycle.append(node)
    for node in range(len(graph)):
        if not visited[node]:
            cycle = []
            dfs(node, -1, visited, cycle)
            if len(cycle) > 1:
                return cycle
    return []

def main():
    n = int(input())
    a = list(map(int, input().split()))
    graph = get_graph(n, a)
    if has_cycle(graph):
        print(-1)
    else:
        cycle = get_shortest_cycle(graph)
        print(len(cycle))

if __name__ == '__main__':
    main()

