
def get_diverse_garland(n, s):
    # Initialize the number of recolors to 0
    recolors = 0
    # Initialize the resulting garland as an empty string
    result = ""
    # Iterate through the input garland
    for i in range(n):
        # If the current lamp is not the same as the previous lamp
        if i == 0 or s[i] != s[i-1]:
            # Add the current lamp to the resulting garland
            result += s[i]
        # If the current lamp is the same as the previous lamp
        else:
            # Increment the number of recolors
            recolors += 1
            # Add the current lamp to the resulting garland
            result += s[i]
    # Return the number of recolors and the resulting garland
    return [recolors, result]

