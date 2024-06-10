distance(n, k, universities, roads):
    from collections import defaultdict

    graph = defaultdict(list)
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)

    distances = []

    def dfs(node, parent, depth):
        nonlocal distances
        if node in universities:
            distances.append(depth)
        for child in graph[node]:
            if child != parent:
                dfs(child, node, depth + 1)

    dfs(universities[0], -1, 0)

    distances.sort(reverse=True)
    print(sum(distances[:k]))

if __name__ == '__main__':
    n, k = map(int, input().split())
    universities = list(map(int, input().split()))
    roads = [list(map(int, input().split())) for _ in range(n - 1)]
    max_distance(n, k, universities, roads)
