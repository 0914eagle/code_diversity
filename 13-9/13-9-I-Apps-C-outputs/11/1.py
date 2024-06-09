
def solve(wheels):
    # Initialize the minimum number of rotations to -1
    min_rotations = -1
    
    # Loop through each column of the first wheel
    for col in range(len(wheels[0])):
        # Initialize a set to store the unique letters in the column
        unique_letters = set()
        
        # Loop through each wheel and add the letter at the current column to the set
        for wheel in wheels:
            unique_letters.add(wheel[col])
        
        # If the set has more than 3 unique letters, return -1
        if len(unique_letters) > 3:
            return -1
    
    # If we reach this point, all columns have at most 3 unique letters, so return the minimum number of rotations
    return min_rotations

