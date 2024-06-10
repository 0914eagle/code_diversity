
def find_unused_switches(n, m, cables):
    graph = {i: [] for i in range(1, n+1)}
    indegree = {i: 0 for i in range(1, n+1)}

    for a, b, _ in cables:
        graph[a].append(b)
        indegree[b] += 1

    stack = [1]
    visited = set()

    while stack:
        node = stack.pop()
        visited.add(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                stack.append(neighbor)

    unused_switches = [i for i in range(1, n+1) if i not in visited]
    return len(unused_switches), unused_switches

if __name__ == '__main__':
    n, m = map(int, input().split())
    cables = [list(map(int, input().split())) for _ in range(m)]
    k, switches = find_unused_switches(n, m, cables)
    print(k)
    print(*switches)
