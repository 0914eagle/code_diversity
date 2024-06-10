
def get_unbalancedness(grid):
    # Initialize variables to keep track of the sums of red and blue numbers
    red_sum = 0
    blue_sum = 0
    
    # Loop through each row of the grid
    for i in range(len(grid)):
        # Loop through each column of the current row
        for j in range(len(grid[i])):
            # If the current square is not the starting square, add the current number to the appropriate sum
            if i != 0 or j != 0:
                if grid[i][j] % 2 == 0:
                    red_sum += grid[i][j]
                else:
                    blue_sum += grid[i][j]
    
    # Return the absolute difference between the two sums
    return abs(red_sum - blue_sum)

def solve(grid):
    # Initialize a variable to keep track of the minimum unbalancedness
    min_unbalancedness = float('inf')
    
    # Loop through each row of the grid
    for i in range(len(grid)):
        # Loop through each column of the current row
        for j in range(len(grid[i])):
            # If the current square is not the starting square, try painting the current square red and blue and check if the unbalancedness is smaller than the current minimum
            if i != 0 or j != 0:
                grid[i][j] = grid[i][j] % 2
                unbalancedness = get_unbalancedness(grid)
                if unbalancedness < min_unbalancedness:
                    min_unbalancedness = unbalancedness
                grid[i][j] = grid[i][j] % 2
    
    # Return the minimum unbalancedness
    return min_unbalancedness

if __name__ == '__main__':
    grid = []
    for _ in range(int(input())):
        grid.append(list(map(int, input().split())))
    result = solve(grid)
    print(result)

