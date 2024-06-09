
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
            if grid[i][j] != '.':
                for k in range(c):
                    if k != grid[i][j]:
                        dp[i][j][k] = min(dp[i][j][k], dp[i][j][grid[i][j]] + barricade_costs[k])

    # Calculate the minimum total cost
    min_cost = float('inf')
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                min_cost = min(min_cost, dp[i][j][grid[i][j]])

    return min_cost

def f2(n, m, c, grid, costs):
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
            if grid[i][j] != '.':
                for k in range(c):
                    if k != grid[i][j]:
                        dp[i][j][k] = min(dp[i][j][k], dp[i][j][grid[i][j]] + barricade_costs[k])

    # Calculate the minimum total cost
    min_cost = float('inf')
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                min_cost = min(min_cost, dp[i][j][grid[i][j]])

    return min_cost

if __name__ == '__main__':
    n, m, c = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(input()))
    costs = list(map(int, input().split()))
    print(f1(n, m, c, grid, costs))
    print(f2(n, m, c, grid, costs))

