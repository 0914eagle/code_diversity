
def solve(s1, s2, s3):
    # Initialize the number of rotations to 0
    rotations = 0

    # Create a set to store the unique letters in each column
    unique_letters = set()

    # Loop through each column of the first wheel
    for i in range(len(s1)):
        # Add the letter in the current column to the set of unique letters
        unique_letters.add(s1[i])

        # If the set has three unique letters, break the loop
        if len(unique_letters) == 3:
            break

    # If the set has three unique letters, return the number of rotations
    if len(unique_letters) == 3:
        return rotations

    # Loop through each column of the second wheel
    for i in range(len(s2)):
        # Add the letter in the current column to the set of unique letters
        unique_letters.add(s2[i])

        # If the set has three unique letters, break the loop
        if len(unique_letters) == 3:
            break

    # If the set has three unique letters, return the number of rotations
    if len(unique_letters) == 3:
        return rotations

    # Loop through each column of the third wheel
    for i in range(len(s3)):
        # Add the letter in the current column to the set of unique letters
        unique_letters.add(s3[i])

        # If the set has three unique letters, break the loop
        if len(unique_letters) == 3:
            break

    # If the set has three unique letters, return the number of rotations
    if len(unique_letters) == 3:
        return rotations

    # If the set does not have three unique letters, return -1
    return -1

