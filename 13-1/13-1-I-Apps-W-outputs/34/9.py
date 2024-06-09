
def f1(n, m, c, grid, costs):
    # Initialize variables
    bank_row, bank_col = -1, -1
    barricade_costs = [0] * c
    for i in range(c):
        barricade_costs[i] = costs[i]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'B':
                bank_row = i
                bank_col = j
                break
        if bank_row != -1:
            break

    # Initialize the dp table
    dp = [[[0] * c for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] != '.':
                dp[i][j][ord(grid[i][j]) - ord('a')] = 1

    # Fill in the dp table
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '.':
                continue
            for k in range(c):
                if dp[i][j][k] == 0:
                    continue
                for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_i = i + dir[0]
                    new_j = j + dir[1]
                    if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] != '.':
                        dp[new_i][new_j][ord(grid[new_i][new_j]) - ord('a')] += dp[i][j][k]

    # Calculate the minimum cost
    min_cost = float('inf')
    for i in range(m):
        for j in range(n):
            if grid[i][j] != '.':
                continue
            total_cost = 0
            for k in range(c):
                if dp[i][j][k] > 0:
                    total_cost += barricade_costs[k]
            if total_cost < min_cost:
                min_cost = total_cost

    return min_cost

def f2(...):
    ...

if __name__ == '__main__':
    n, m, c = map(int, input().split())
    grid = []
    for i in range(m):
        grid.append(list(input()))
    costs = list(map(int, input().split()))
    print(f1(n, m, c, grid, costs))

