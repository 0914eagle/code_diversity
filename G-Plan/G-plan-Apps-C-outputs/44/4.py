_unused_switches(n, m, cables):
    graph = {i: [] for i in range(1, n + 1)}
    indegree = {i: 0 for i in range(1, n + 1)}

    for a, b, _ in cables:
        graph[a].append(b)
        indegree[b] += 1

    queue = [i for i in range(1, n + 1) if indegree[i] == 0]
    unused_switches = set()

    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    for switch, degree in indegree.items():
        if degree > 0 and switch != n:
            unused_switches.add(switch)

    return unused_switches


def main():
    n, m = map(int, input().split())
    cables = [list(map(int, input().split())) for _ in range(m)]

    unused_switches = find_unused_switches(n, m, cables)

    print(len(unused_switches))
    print(*sorted(unused_switches))


if __name__ == '__main__':
    main()
