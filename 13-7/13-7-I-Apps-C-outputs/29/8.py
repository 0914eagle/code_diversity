
def get_cycles(graph):
    visited = [False] * len(graph)
    cycles = []
    for i in range(len(graph)):
        if not visited[i]:
            cycle = []
            dfs(graph, i, visited, cycle)
            if len(cycle) > 0:
                cycles.append(cycle)
    return cycles

def dfs(graph, node, visited, cycle):
    visited[node] = True
    cycle.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, cycle)
    return cycle

def shortest_cycle(graph):
    cycles = get_cycles(graph)
    if len(cycles) == 0:
        return -1
    return min(len(cycle) for cycle in cycles)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if a[i] & a[j] != 0:
                graph[i].append(j)
                graph[j].append(i)
    print(shortest_cycle(graph))

if __name__ == '__main__':
    main()

