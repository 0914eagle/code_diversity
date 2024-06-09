
def f1(n, m, c, grid, costs):
    # Initialize the minimum total cost to prevent the robbers from escaping
    min_cost = float('inf')
    
    # Loop through each cell in the grid
    for i in range(n):
        for j in range(m):
            # If the current cell is the bank, continue to the next cell
            if grid[i][j] == 'B':
                continue
            # If the current cell is a dot, continue to the next cell
            if grid[i][j] == '.':
                continue
            # If the current cell is not the bank or a dot, calculate the minimum cost to barricade the cell
            cost = calculate_cost(i, j, grid, costs)
            # If the minimum cost is less than the current minimum cost, update the minimum cost
            if cost < min_cost:
                min_cost = cost
    
    # Return the minimum total cost to prevent the robbers from escaping
    return min_cost

def f2(n, m, c, grid, costs):
    # Initialize the minimum total cost to prevent the robbers from escaping
    min_cost = float('inf')
    
    # Loop through each cell in the grid
    for i in range(n):
        for j in range(m):
            # If the current cell is the bank, continue to the next cell
            if grid[i][j] == 'B':
                continue
            # If the current cell is a dot, continue to the next cell
            if grid[i][j] == '.':
                continue
            # If the current cell is not the bank or a dot, calculate the minimum cost to barricade the cell
            cost = calculate_cost(i, j, grid, costs)
            # If the minimum cost is less than the current minimum cost, update the minimum cost
            if cost < min_cost:
                min_cost = cost
    
    # Return the minimum total cost to prevent the robbers from escaping
    return min_cost

def calculate_cost(i, j, grid, costs):
    # Initialize the minimum cost to barricade the cell
    min_cost = 0
    
    # If the cell is not on the border of the grid, calculate the cost to barricade the cell
    if i > 0 and i < n-1 and j > 0 and j < m-1:
        # Loop through each direction (up, down, left, right)
        for direction in ['up', 'down', 'left', 'right']:
            # If the cell in the current direction is not the bank or a dot, calculate the cost to barricade the cell in the current direction
            if grid[i+direction[0]][j+direction[1]] != 'B' and grid[i+direction[0]][j+direction[1]] != '.':
                # Add the cost of barricading the cell in the current direction to the minimum cost
                min_cost += costs[ord(grid[i+direction[0]][j+direction[1]])-ord('a')]
    
    # Return the minimum cost to barricade the cell
    return min_cost

if __name__ == '__main__':
    n, m, c = map(int, input().split())
    grid = [input() for _ in range(n)]
    costs = list(map(int, input().split()))
    print(f1(n, m, c, grid, costs))
    print(f2(n, m, c, grid, costs))

