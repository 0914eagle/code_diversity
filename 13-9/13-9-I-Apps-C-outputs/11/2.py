
def solve(wheels):
    # Initialize the minimum number of rotations to -1
    min_rotations = -1
    
    # Iterate through each column of the first wheel
    for col in range(len(wheels[0])):
        # Initialize a set to store the unique letters in the column
        unique_letters = set()
        
        # Iterate through each wheel
        for wheel in wheels:
            # Add the letter at the current column to the set
            unique_letters.add(wheel[col])
        
        # If the set has three unique letters, return the minimum number of rotations
        if len(unique_letters) == 3:
            return min_rotations
    
    # If we reach this point, it isn't possible to have three unique letters in every column, so return -1
    return min_rotations

