
def count_ways(n, m, q, runs, queries):
    graph = {i: [] for i in range(1, n + 1)}
    for run in runs:
        x, y = run
        graph[x].append(y)

    def dfs(node, snack_stands, areas):
        if not areas:
            return 1 if snack_stands == 0 else 0
        if snack_stands == 0:
            return 0
        ways = 0
        for neighbor in graph[node]:
            ways += dfs(neighbor, snack_stands - (neighbor in areas), areas - {neighbor})
        return ways

    results = []
    for query in queries:
        k, a, *areas = query
        ways = sum(dfs(1, k, set(areas)))
        results.append(ways)
    return results

if __name__ == "__main__":
    n, m, q = map(int, input().split())
    runs = [tuple(map(int, input().split())) for _ in range(m)]
    queries = [list(map(int, input().split())) for _ in range(q)]
    output = count_ways(n, m, q, runs, queries)
    for result in output:
        print(result)
