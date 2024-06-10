_unused_switches(n, cables):
    graph = {i: [] for i in range(1, n + 1)}
    for a, b, _ in cables:
        graph[a].append(b)

    indegree = {i: 0 for i in range(1, n + 1)}
    for a, b, _ in cables:
        indegree[b] += 1

    unused_switches = [i for i in range(1, n + 1) if indegree[i] == 0]
    return unused_switches


def main():
    n, m = map(int, input().split())
    cables = [list(map(int, input().split())) for _ in range(m)]

    unused_switches = find_unused_switches(n, cables)

    print(len(unused_switches))
    print(*unused_switches)


if __name__ == '__main__':
    main()
""