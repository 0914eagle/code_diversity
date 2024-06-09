
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

    # Initialize the minimum cost to infinity
    min_cost = float('inf')

    # Iterate through all possible barricade configurations
    for configuration in range(1 << c):
        # Calculate the cost of the current barricade configuration
        cost = 0
        for i in range(c):
            if configuration & (1 << i):
                cost += barricade_costs[i]

        # Check if the current barricade configuration prevents the robbers from escaping
        if not any(grid[bank_row + dr][bank_col + dc] == '.' for dr in range(-1, 2) for dc in range(-1, 2) if 0 <= bank_row + dr < n and 0 <= bank_col + dc < m):
            min_cost = min(min_cost, cost)

    # Return the minimum cost
    return min_cost if min_cost < float('inf') else -1

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    n, m, c = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(input()))
    costs = list(map(int, input().split()))
    print(f1(n, m, c, grid, costs))

