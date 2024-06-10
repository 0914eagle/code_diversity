t_ways_to_stock_snack_stands(n, m, q, runs, queries):
    graph = {i: [] for i in range(1, n + 1)}
    for x, y in runs:
        graph[x].append(y)

    def dfs(node, snack_stands, areas):
        if len(areas) == 0:
            return 1 if snack_stands == 0 else 0
        if snack_stands == 0:
            return 0
        ways = 0
        for neighbor in graph[node]:
            ways += dfs(neighbor, snack_stands - 1, [area for area in areas if area != neighbor])
        return ways

    results = []
    for k, a, *areas in queries:
        ways = 0
        for start_area in areas:
            ways += dfs(start_area, k - 1, [area for area in areas if area != start_area])
        results.append(ways)

    return results


if __name__ == "__main__":
    n, m, q = map(int, input().split())
    runs = [tuple(map(int, input().split())) for _ in range(m)]
    queries = [list(map(int, input().split())) for _ in range(q)]
    
    results = count_ways_to_stock_snack_stands(n, m, q, runs, queries)
    for result in results:
        print(result