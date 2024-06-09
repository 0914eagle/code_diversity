
def get_final_state(grid):
    # Initialize the final state as an empty string
    final_state = ""
    
    # Loop through each row of the grid
    for row in grid:
        # If the row is not empty, add it to the final state
        if row != "":
            final_state += row + "\n"
    
    # Return the final state
    return final_state.strip()

def main():
    # Read the input grid from stdin
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    
    # Get the final state of the grid
    final_state = get_final_state(grid)
    
    # Print the final state
    print(final_state)

if __name__ == '__main__':
    main()

