
def get_unbalancedness(grid):
    # Initialize variables to track the sums of red and blue numbers
    red_sum, blue_sum = 0, 0
    
    # Loop through the grid and calculate the sum of red and blue numbers
    for row in grid:
        for num in row:
            if num % 2 == 0:
                red_sum += num
            else:
                blue_sum += num
    
    # Return the absolute difference between the two sums
    return abs(red_sum - blue_sum)

def solve(grid):
    # Initialize a variable to track the minimum unbalancedness
    min_unbalancedness = float('inf')
    
    # Loop through all possible combinations of red and blue numbers
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current square has an even number, paint it red
            if grid[i][j] % 2 == 0:
                grid[i][j] = 1
            # If the current square has an odd number, paint it blue
            else:
                grid[i][j] = 0
    
    # Calculate the unbalancedness for the current grid configuration
    unbalancedness = get_unbalancedness(grid)
    
    # If the current unbalancedness is less than the minimum unbalancedness, update the minimum unbalancedness
    if unbalancedness < min_unbalancedness:
        min_unbalancedness = unbalancedness
    
    # Return the minimum unbalancedness
    return min_unbalancedness

if __name__ == '__main__':
    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append(list(map(int, input().split())))
    print(solve(grid))

