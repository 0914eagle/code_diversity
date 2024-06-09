
def get_wrongness(color_grid, D):
    # Initialize the sum of wrongness to 0
    wrongness_sum = 0
    
    # Loop through each row of the grid
    for i in range(len(color_grid)):
        # Loop through each column of the grid
        for j in range(len(color_grid[i])):
            # Get the current color of the square
            current_color = color_grid[i][j]
            
            # Loop through each row and column that is not the current row or column
            for x in range(len(color_grid)):
                for y in range(len(color_grid[x])):
                    # If the current row and column are not the same as the row and column being compared
                    if i != x or j != y:
                        # Get the color of the square being compared
                        compare_color = color_grid[x][y]
                        
                        # If the current color and the compare color are the same
                        if current_color == compare_color:
                            # Add the wrongness of the current square and the square being compared to the sum of wrongness
                            wrongness_sum += D[current_color - 1][compare_color - 1]
    
    # Return the sum of wrongness
    return wrongness_sum

def solve(N, C, D, color_grid):
    # Initialize the minimum possible sum of wrongness to a large value
    min_wrongness_sum = 1000
    
    # Loop through each possible color for the current square
    for i in range(1, C + 1):
        # Loop through each possible color for the compare square
        for j in range(1, C + 1):
            # If the current color and the compare color are different
            if i != j:
                # Get the wrongness of the current square and the compare square
                wrongness = D[i - 1][j - 1]
                
                # Loop through each row of the grid
                for x in range(len(color_grid)):
                    # Loop through each column of the grid
                    for y in range(len(color_grid[x])):
                        # If the current color of the square is the same as the current color being tested
                        if color_grid[x][y] == i:
                            # Replace the current color of the square with the compare color
                            color_grid[x][y] = j
                            
                            # Get the sum of wrongness of the updated grid
                            wrongness_sum = get_wrongness(color_grid, D)
                            
                            # If the sum of wrongness is less than the minimum possible sum of wrongness
                            if wrongness_sum < min_wrongness_sum:
                                # Update the minimum possible sum of wrongness
                                min_wrongness_sum = wrongness_sum
                            
                            # Replace the current color of the square with the original color
                            color_grid[x][y] = i
    
    # Return the minimum possible sum of wrongness
    return min_wrongness_sum

if __name__ == '__main__':
    # Read the input
    N, C = map(int, input().split())
    D = []
    for i in range(C):
        D.append(list(map(int, input().split())))
    color_grid = []
    for i in range(N):
        color_grid.append(list(map(int, input().split())))
    
    # Solve the problem
    result = solve(N, C, D, color_grid)
    
    # Output the result
    print(result)

