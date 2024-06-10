
def get_unbalancedness(grid):
    # Initialize variables to keep track of the sums of red and blue numbers
    red_sum = 0
    blue_sum = 0
    
    # Loop through the grid and calculate the sums of red and blue numbers
    for row in grid:
        for num in row:
            if num % 2 == 0:
                red_sum += num
            else:
                blue_sum += num
    
    # Return the absolute difference between the sums of red and blue numbers
    return abs(red_sum - blue_sum)

def solve(grid):
    # Initialize a variable to keep track of the minimum unbalancedness
    min_unbalancedness = float('inf')
    
    # Loop through the grid and check all possible combinations of red and blue numbers
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the number at the current position is even, paint it red
            if grid[i][j] % 2 == 0:
                grid[i][j] = 1
            # If the number at the current position is odd, paint it blue
            else:
                grid[i][j] = 0
                
            # Calculate the unbalancedness of the current grid
            unbalancedness = get_unbalancedness(grid)
            
            # If the current unbalancedness is less than the minimum unbalancedness, update the minimum unbalancedness
            if unbalancedness < min_unbalancedness:
                min_unbalancedness = unbalancedness
    
    # Return the minimum unbalancedness
    return min_unbalancedness

if __name__ == '__main__':
    grid = []
    
    # Read the input from stdin
    for _ in range(int(input())):
        grid.append(list(map(int, input().split())))
    
    # Solve the problem
    print(solve(grid))

