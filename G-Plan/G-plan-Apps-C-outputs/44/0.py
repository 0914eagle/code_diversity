
def find_unused_switches(n, cables):
    graph = {i: [] for i in range(1, n + 1)}
    indegree = {i: 0 for i in range(1, n + 1)}

    for a, b, _ in cables:
        graph[a].append(b)
        indegree[b] += 1

    stack = [i for i in range(1, n + 1) if indegree[i] == 0]
    unused_switches = set()

    while stack:
        node = stack.pop()
        unused_switches.add(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                stack.append(neighbor)

    return unused_switches


def main():
    n, m = map(int, input().split())
    cables = [list(map(int, input().split())) for _ in range(m)]

    unused_switches = find_unused_switches(n, cables)

    print(len(unused_switches))
    print(*sorted(unused_switches))


if __name__ == '__main__':
    main()
