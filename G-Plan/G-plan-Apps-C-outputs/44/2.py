
def find_unused_switches(n, m, cables):
    graph = {}
    for a, b, _ in cables:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)

    indegree = {node: 0 for node in graph}
    for _, b, _ in cables:
        indegree[b] += 1

    queue = [1]
    unused = set(range(1, n + 1))
    while queue:
        node = queue.pop(0)
        if node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        unused.discard(node)

    return len(unused) - 1, sorted(unused)


if __name__ == '__main__':
    n, m = map(int, input().split())
    cables = [list(map(int, input().split())) for _ in range(m)]
    k, unused_switches = find_unused_switches(n, m, cables)
    print(k)
    print(*unused_switches)
