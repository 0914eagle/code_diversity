
def f1(n, m, c, grid, costs):
    # Initialize variables
    bank_row, bank_col = -1, -1
    barricade_costs = [0] * c
    for i in range(c):
        barricade_costs[i] = costs[i]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B':
                bank_row = i
                bank_col = j
                break
        if bank_row != -1:
            break

    # Initialize the dp table
    dp = [[[0] * c for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                dp[i][j][grid[i][j]] = barricade_costs[grid[i][j]]

    # Fill in the dp table
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                continue
            for k in range(c):
                if k == grid[i][j]:
                    continue
                dp[i][j][k] = min(dp[i][j][k], dp[i][j][grid[i][j]] + barricade_costs[k])
            for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_i = i + dir[0]
                new_j = j + dir[1]
                if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] != '.':
                    dp[i][j][grid[new_i][new_j]] = min(dp[i][j][grid[new_i][new_j]], dp[i][j][grid[i][j]] + barricade_costs[grid[new_i][new_j]])

    # Find the minimum total cost
    min_cost = float('inf')
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                min_cost = min(min_cost, dp[i][j][grid[i][j]])

    return -1 if min_cost == float('inf') else min_cost

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    n, m, c = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(input()))
    costs = list(map(int, input().split()))
    print(f1(n, m, c, grid, costs))

