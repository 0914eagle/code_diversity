
def get_final_state(grid):
    # Initialize the final state as an empty list
    final_state = []
    
    # Loop through each row in the grid
    for row in grid:
        # Check if the row is all white
        if all(cell == "." for cell in row):
            # If it is, skip this row
            continue
        # If the row is not all white, add it to the final state
        final_state.append(row)
    
    # Loop through each column in the grid
    for col in range(len(grid[0])):
        # Check if the column is all white
        if all(row[col] == "." for row in grid):
            # If it is, skip this column
            continue
        # If the column is not all white, add it to the final state
        for row in final_state:
            row.append(grid[row.index(row[0])][col])
    
    # Return the final state
    return final_state

def main():
    # Read the input grid from stdin
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    
    # Get the final state of the grid
    final_state = get_final_state(grid)
    
    # Print the final state
    for row in final_state:
        print("".join(row))

if __name__ == '__main__':
    main()

