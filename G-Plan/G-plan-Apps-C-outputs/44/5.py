_unused_switches(n, m, cables):
    graph = {i: [] for i in range(1, n + 1)}
    for a, b, _ in cables:
        graph[a].append(b)

    def dfs(node, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)

    visited = set()
    dfs(1, visited)

    unused_switches = [str(i) for i in range(1, n + 1) if i not in visited]
    return len(unused_switches), unused_switches

if __name__ == '__main__':
    n, m = map(int, input().split())
    cables = [list(map(int, input().split())) for _ in range(m)]
    k, unused_switches = find_unused_switches(n, m, cables)
    print(k)
    print(' '.join(unused_switches))
