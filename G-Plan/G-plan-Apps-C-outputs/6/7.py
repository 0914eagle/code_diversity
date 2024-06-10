e_query(n, m, q, runs, queries):
    adj_list = {i: [] for i in range(1, n + 1)}
    for x, y in runs:
        adj_list[x].append(y)

    def dfs(node, snack_stands, areas):
        if not areas:
            return 1 if snack_stands == 0 else 0
        if snack_stands == 0:
            return 0
        ways = 0
        for neighbor in adj_list[node]:
            ways += dfs(neighbor, snack_stands - (neighbor in areas), areas - {neighbor})
        return ways

    results = []
    for k, a, *areas in queries:
        ways = 0
        for start_node in adj_list[1]:
            ways += dfs(start_node, k - 1, set(areas) - {start_node})
        results.append(ways)

    return results


if __name__ == "__main__":
    n, m, q = map(int, input().split())
    runs = [tuple(map(int, input().split())) for _ in range(m)]
    queries = [list(map(int, input().split())) for _ in range(q)]

    results = solve_query(n, m, q, runs, queries)
    for result in results:
        print(result)
