
def solve(wheels):
    # Initialize the minimum number of rotations required to -1
    min_rotations = -1
    
    # Iterate over each column of the wheels
    for col in range(len(wheels[0])):
        # Get the letters in the current column
        letters = [wheel[col] for wheel in wheels]
        
        # Check if the letters in the current column are all distinct
        if len(set(letters)) == 3:
            # If they are, continue to the next column
            continue
        else:
            # If they are not, rotate the wheels to the right by one column
            wheels = [wheel[1:] + wheel[:1] for wheel in wheels]
            min_rotations += 1
    
    # Return the minimum number of rotations required
    return min_rotations

