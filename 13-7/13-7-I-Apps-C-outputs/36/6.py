
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

def remove_corridors(graph, m):
    cycles = get_cycles(graph)
    removed_corridors = 0
    removed_edges = []
    for cycle in cycles:
        if len(cycle) > 1:
            for i in range(len(cycle) - 1):
                edge = (cycle[i], cycle[i + 1])
                if edge not in removed_edges:
                    removed_edges.append(edge)
                    removed_corridors += 1
                    if removed_corridors == m / 2:
                        return removed_edges
    return removed_edges

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    removed_edges = remove_corridors(graph, m)
    print(len(removed_edges))
    for edge in removed_edges:
        print(*edge)

if __name__ == '__main__':
    main()

