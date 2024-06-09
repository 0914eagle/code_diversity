
def solve_coin_problem(grid):
    # Initialize variables
    max_even_cells = 0
    operations = []

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the cell contains an even number of coins, increment the maximum number of even cells
            if grid[i][j] % 2 == 0:
                max_even_cells += 1
            # If the cell contains an odd number of coins, try to move a coin to an adjacent cell
            else:
                # Check if the cell has an adjacent cell with an even number of coins
                for k in range(len(grid)):
                    if grid[i][(j-1)%len(grid[0])] % 2 == 0:
                        # Move the coin to the adjacent cell with an even number of coins
                        grid[i][j] -= 1
                        grid[i][(j-1)%len(grid[0])] += 1
                        operations.append([i, j, i, (j-1)%len(grid[0])])
                        break
                    elif grid[i][(j+1)%len(grid[0])] % 2 == 0:
                        # Move the coin to the adjacent cell with an even number of coins
                        grid[i][j] -= 1
                        grid[i][(j+1)%len(grid[0])] += 1
                        operations.append([i, j, i, (j+1)%len(grid[0])])
                        break
                    elif grid[(i-1)%len(grid)][(j-1)%len(grid[0])] % 2 == 0:
                        # Move the coin to the adjacent cell with an even number of coins
                        grid[i][j] -= 1
                        grid[(i-1)%len(grid)][(j-1)%len(grid[0])] += 1
                        operations.append([i, j, (i-1)%len(grid), (j-1)%len(grid[0])])
                        break
                    elif grid[(i-1)%len(grid)][(j+1)%len(grid[0])] % 2 == 0:
                        # Move the coin to the adjacent cell with an even number of coins
                        grid[i][j] -= 1
                        grid[(i-1)%len(grid)][(j+1)%len(grid[0])] += 1
                        operations.append([i, j, (i-1)%len(grid), (j+1)%len(grid[0])])
                        break
                    elif grid[(i+1)%len(grid)][(j-1)%len(grid[0])] % 2 == 0:
                        # Move the coin to the adjacent cell with an even number of coins
                        grid[i][j] -= 1
                        grid[(i+1)%len(grid)][(j-1)%len(grid[0])] += 1
                        operations.append([i, j, (i+1)%len(grid), (j-1)%len(grid[0])])
                        break
                    elif grid[(i+1)%len(grid)][(j+1)%len(grid[0])] % 2 == 0:
                        # Move the coin to the adjacent cell with an even number of coins
                        grid[i][j] -= 1
                        grid[(i+1)%len(grid)][(j+1)%len(grid[0])] += 1
                        operations.append([i, j, (i+1)%len(grid), (j+1)%len(grid[0])])
                        break

    # Return the maximum number of even cells and the sequence of operations
    return [max_even_cells, operations]

