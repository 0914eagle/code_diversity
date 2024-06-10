distance(towns, universities, roads):
    graph = {i: [] for i in range(1, towns + 1)}
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)

    def dfs(node, parent, distances):
        nonlocal max_sum
        if node in universities:
            distances.append(0)
        for neighbor in graph[node]:
            if neighbor != parent:
                dfs(neighbor, node, distances)
        if distances:
            max_sum += max(distances) + 1
            distances.pop()

    max_sum = 0
    dfs(universities[0], -1, [])
    return max_sum

if __name__ == "__main__":
    n, k = map(int, input().split())
    universities = list(map(int, input().split()))
    roads = [list(map(int, input().split())) for _ in range(n - 1)]
    print(max_distance(n, universities, roads))
