ulate_rebuilds(n, m, roads, k, path):
    intersections = set(path)
    rebuilds_min = 0
    rebuilds_max = 0

    for i in range(k - 1):
        if (path[i], path[i + 1]) not in roads and (path[i + 1], path[i]) not in roads:
            rebuilds_min += 1
            rebuilds_max += 1
        elif path[i + 1] not in intersections:
            rebuilds_max += 1

    return rebuilds_min, rebuilds_max

if __name__ == '__main__':
    n, m = map(int, input().split())
    roads = set()
    for _ in range(m):
        u, v = map(int, input().split())
        roads.add((u, v))
    
    k = int(input())
    path = list(map(int, input().split()))

    min_rebuilds, max_rebuilds = calculate_rebuilds(n, m, roads, k, path)
    print(min_rebuilds, max_rebuilds)
