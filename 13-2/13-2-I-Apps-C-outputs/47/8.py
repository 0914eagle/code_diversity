
def get_trail(grid, program, start_row, start_col):
    # Initialize the trail as a list containing the starting location
    trail = [(start_row, start_col)]
    
    # Loop through the program
    for char in program:
        # Get the current location
        row, col = trail[-1]
        
        # Check if the character is a movement command
        if char in ["<", ">", "^", "v"]:
            # Get the new location based on the movement command
            if char == "<":
                col -= 1
            elif char == ">":
                col += 1
            elif char == "^":
                row -= 1
            elif char == "v":
                row += 1
            
            # Check if the new location is valid
            if grid[row][col] == ".":
                # Add the new location to the trail
                trail.append((row, col))
            else:
                # Skip the movement if the new location is invalid
                continue
        else:
            # If the character is not a movement command, skip it
            continue
    
    # Return the trail
    return trail

def get_repetition_length(trail):
    # Initialize the repetition length as 1
    repetition_length = 1
    
    # Loop through the trail
    for i in range(len(trail)):
        # Check if the suffix of the trail starting from the current index is a repetition of the trail
        if trail[i:] == trail[:len(trail) - i]:
            # If it is, return the repetition length
            return repetition_length
        else:
            # If it is not, increment the repetition length
            repetition_length += 1
    
    # If the trail does not repeat, return 0
    return 0

def main():
    # Read the input
    N, program = input().split()
    grid = [input() for _ in range(int(N))]
    
    # Get the starting location of the robot
    start_row, start_col = None, None
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "R":
                start_row, start_col = row, col
                break
    
    # Get the trail of the robot
    trail = get_trail(grid, program, start_row, start_col)
    
    # Get the repetition length of the trail
    repetition_length = get_repetition_length(trail)
    
    # Print the output
    if repetition_length == 0:
        print(1)
    else:
        print(repetition_length)

if __name__ == '__main__':
    main()

