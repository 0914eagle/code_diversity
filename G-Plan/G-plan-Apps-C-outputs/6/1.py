t_ways_to_stock_snack_stands(n, m, q, ski_runs, queries):
    graph = {i: [] for i in range(1, n + 1)}
    for x, y in ski_runs:
        graph[x].append(y)

    def dfs(node, query_areas, k):
        if k == 0:
            return 0
        if node in query_areas:
            k -= 1
        if k == 0:
            return 1
        ways = 0
        for neighbor in graph[node]:
            ways += dfs(neighbor, query_areas, k)
        return ways

    results = []
    for query in queries:
        k, a, *areas = query
        query_areas = set(areas)
        ways = 0
        for area in query_areas:
            ways += dfs(area, query_areas, k)
        results.append(ways)

    return results


if __name__ == "__main__":
    n, m, q = map(int, input().split())
    ski_runs = [tuple(map(int, input().split())) for _ in range(m)]
    queries = [list(map(int, input().split()))[1:] for _ in range(q)]

    results = count_ways_to_stock_snack_stands(n, m, q, ski_runs, queries)
    for result in results:
        print(result)
