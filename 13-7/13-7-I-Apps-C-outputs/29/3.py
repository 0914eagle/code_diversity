
def get_graph(n, a):
    graph = {}
    for i in range(n):
        for j in range(i+1, n):
            if a[i] & a[j] != 0:
                graph[i] = graph.get(i, []) + [j]
                graph[j] = graph.get(j, []) + [i]
    return graph

def has_cycle(graph):
    visited = [False] * len(graph)
    def dfs(i, visited):
        if visited[i]:
            return True
        visited[i] = True
        for j in graph[i]:
            if dfs(j, visited):
                return True
        return False
    for i in range(len(graph)):
        if dfs(i, visited):
            return True
    return False

def get_cycle_length(graph):
    visited = [False] * len(graph)
    def dfs(i, visited, cycle):
        if visited[i]:
            return
        visited[i] = True
        for j in graph[i]:
            if not visited[j]:
                dfs(j, visited, cycle + [j])
            else:
                for k in range(len(cycle)):
                    if cycle[k] == j:
                        return len(cycle[k:])
        return 0
    for i in range(len(graph)):
        if not visited[i]:
            cycle = dfs(i, visited, [i])
            if cycle:
                return cycle
    return -1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    graph = get_graph(n, a)
    if has_cycle(graph):
        print(get_cycle_length(graph))
    else:
        print(-1)

if __name__ == '__main__':
    main()

