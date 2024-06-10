ulate_rebuilds(n, m, roads, k, path):
    intersections = set(path)
    rebuilds_min = 0
    rebuilds_max = 0

    for i in range(k - 1):
        if path[i + 1] not in roads[path[i]]:
            rebuilds_min += 1
            rebuilds_max += len(roads[path[i]]) - 1

    print(rebuilds_min, rebuilds_max)


if __name__ == "__main__":
    n, m = map(int, input().split())
    roads = {i: set() for i in range(1, n + 1)}

    for _ in range(m):
        u, v = map(int, input().split())
        roads[u].add(v)
        roads[v].add(u)

    k = int(input())
    path = list(map(int, input().split()))

    calculate_rebuilds(n, m, roads, k, path)
