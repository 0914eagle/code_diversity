
def get_final_state(grid):
    # Initialize the final state as an empty string
    final_state = ""
    
    # Loop through each row of the grid
    for i in range(len(grid)):
        # Check if the row is all white
        if all(cell == "." for cell in grid[i]):
            # If it is, skip this row
            continue
        # If the row is not all white, add it to the final state
        final_state += "".join(grid[i]) + "\n"
    
    # Loop through each column of the grid
    for j in range(len(grid[0])):
        # Check if the column is all white
        if all(row[j] == "." for row in grid):
            # If it is, skip this column
            continue
        # If the column is not all white, add it to the final state
        final_state += "".join(row[j] for row in grid) + "\n"
    
    # Return the final state
    return final_state.strip()

def main():
    # Read the input grid from stdin
    grid = [input().split() for _ in range(int(input()))]
    
    # Get the final state of the grid
    final_state = get_final_state(grid)
    
    # Print the final state
    print(final_state)

if __name__ == '__main__':
    main()

