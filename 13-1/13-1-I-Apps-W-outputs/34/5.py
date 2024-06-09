
def f1(n, m, c, grid, costs):
    # Initialize variables
    bank_row, bank_col = -1, -1
    barricade_costs = [0] * c
    for i in range(c):
        barricade_costs[i] = costs[i]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B':
                bank_row, bank_col = i, j
                break
        if bank_row != -1:
            break

    # Initialize the barricade matrix
    barricade_matrix = [[0] * c for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                barricade_matrix[i][j] = 1

    # Initialize the cost matrix
    cost_matrix = [[0] * c for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                cost_matrix[i][j] = barricade_costs[ord(grid[i][j]) - ord('a')]

    # Solve the problem using dynamic programming
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                for k in range(c):
                    if barricade_matrix[i][j] == 0:
                        cost_matrix[i][j] = min(cost_matrix[i][j], cost_matrix[i - 1][j] + barricade_costs[k])
                        cost_matrix[i][j] = min(cost_matrix[i][j], cost_matrix[i + 1][j] + barricade_costs[k])
                        cost_matrix[i][j] = min(cost_matrix[i][j], cost_matrix[i][j - 1] + barricade_costs[k])
                        cost_matrix[i][j] = min(cost_matrix[i][j], cost_matrix[i][j + 1] + barricade_costs[k])

    # Return the minimum total cost
    return cost_matrix[bank_row][bank_col]

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

