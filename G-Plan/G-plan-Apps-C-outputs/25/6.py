distance(towns, pairs, universities, roads):
    from collections import defaultdict

    graph = defaultdict(list)
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)

    def dfs(node, parent, dist):
        max_dist = dist
        for neighbor in graph[node]:
            if neighbor != parent:
                max_dist = max(max_dist, dfs(neighbor, node, dist + 1))
        return max_dist

    distances = []
    for i in range(0, len(universities), 2):
        u1, u2 = universities[i], universities[i + 1]
        dist1 = dfs(u1, -1, 0)
        dist2 = dfs(u2, -1, 0)
        distances.append(dist1 + dist2)

    distances.sort(reverse=True)
    return sum(distances[:pairs])


if __name__ == "__main__":
    n, k = map(int, input().split())
    universities = list(map(int, input().split()))
    roads = [list(map(int, input().split())) for _ in range(n - 1)]

    result = max_distance(n, k, universities, roads)
    print(result)
