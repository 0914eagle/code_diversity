
def count_black_squares(grid, k):
    # Initialize a counter for the number of black squares
    black_squares = 0
    
    # Loop through each row in the grid
    for i in range(len(grid)):
        # Loop through each column in the row
        for j in range(len(grid[i])):
            # If the current square is black, increment the counter
            if grid[i][j] == '#':
                black_squares += 1
    
    # Return the number of black squares
    return black_squares

def count_choices(grid, k):
    # Initialize a counter for the number of choices
    choices = 0
    
    # Loop through each row in the grid
    for i in range(len(grid)):
        # Loop through each column in the row
        for j in range(len(grid[i])):
            # If the current square is black, increment the counter
            if grid[i][j] == '#':
                choices += 1
    
    # Return the number of choices
    return choices

def main():
    # Read the input grid and the number of black squares from stdin
    grid = [input() for _ in range(int(input()))]
    k = int(input())
    
    # Call the count_black_squares function to count the number of black squares in the grid
    black_squares = count_black_squares(grid, k)
    
    # Call the count_choices function to count the number of choices of rows and columns that result in exactly k black squares
    choices = count_choices(grid, k)
    
    # Print the number of choices
    print(choices)

if __name__ == '__main__':
    main()

