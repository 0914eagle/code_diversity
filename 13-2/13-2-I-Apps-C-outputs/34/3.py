
def solve(grid):
    # Initialize the minimum number of moves to infinity
    min_moves = float('inf')
    # Initialize the optimal solution as an empty list
    optimal_solution = []
    
    # Loop through each possible move (row or column)
    for move in range(1, len(grid) + 1):
        # Check if the move is valid (i.e., the move is within the bounds of the grid)
        if move <= len(grid):
            # Clone the grid to prevent modifying the original grid
            grid_clone = grid.copy()
            # Perform the move by adding 1 to all cells in the selected row or column
            for i in range(len(grid_clone)):
                if move == 1:
                    grid_clone[i][move - 1] += 1
                else:
                    grid_clone[move - 1][i] += 1
            # Check if the grid is solved after the move
            if is_solved(grid_clone):
                # If the grid is solved, update the minimum number of moves and the optimal solution
                min_moves = 1
                optimal_solution = [move]
                break
            # If the grid is not solved, check if the number of moves is less than the current minimum
            elif len(optimal_solution) == 0 or len(optimal_solution) > min_moves + 1:
                # If the number of moves is less than the current minimum, update the minimum number of moves and the optimal solution
                min_moves += 1
                optimal_solution = [move]
    
    # Return the optimal solution
    return optimal_solution

def is_solved(grid):
    # Check if all cells in the grid are equal to the target value
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != grid[0][0]:
                return False
    return True

def main():
    # Read the input grid from stdin
    grid = []
    for _ in range(int(input())):
        grid.append(list(map(int, input().split())))
    
    # Solve the grid and print the result
    solution = solve(grid)
    if len(solution) == 0:
        print(-1)
    else:
        print(len(solution))
        for move in solution:
            print(move)

if __name__ == "__main__":
    main()

