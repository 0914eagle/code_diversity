
def get_final_state(grid):
    # Initialize the final state as an empty string
    final_state = ""
    
    # Loop through each row of the grid
    for i in range(len(grid)):
        # Loop through each column of the row
        for j in range(len(grid[i])):
            # If the current square is black, add it to the final state
            if grid[i][j] == "#":
                final_state += "#"
            # If the current square is white and it is not the last square in the row, add a space to the final state
            elif grid[i][j] == "." and j != len(grid[i]) - 1:
                final_state += " "
    
    # Return the final state
    return final_state

def main():
    # Read the input grid from stdin
    grid = [input() for _ in range(int(input()))]
    
    # Get the final state of the grid
    final_state = get_final_state(grid)
    
    # Print the final state
    print(final_state)

if __name__ == '__main__':
    main()

