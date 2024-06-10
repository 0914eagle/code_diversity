t_ways_to_stock_snack_stands(n, m, q, runs, queries):
    graph = {i: [] for i in range(1, n + 1)}
    for x, y in runs:
        graph[x].append(y)

    def dfs(node, query_areas, k):
        if k == 0:
            return 0 if node not in query_areas else 1
        count = 0
        for neighbor in graph[node]:
            count += dfs(neighbor, query_areas, k - 1)
        return count

    results = []
    for k, a, *areas in queries:
        total_ways = 0
        for area in areas:
            total_ways += dfs(1, set(areas), k - 1)
        results.append(total_ways)

    return results


if __name__ == "__main__":
    n, m, q = map(int, input().split())
    runs = [tuple(map(int, input().split())) for _ in range(m)]
    queries = [list(map(int, input().split())) for _ in range(q)]

    results = count_ways_to_stock_snack_stands(n, m, q, runs, queries)
    for result in results:
        print(result