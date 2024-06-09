
def get_diverse_garland(n, s):
    # Initialize the number of recolors to 0
    recolors = 0
    # Initialize the diverse garland as an empty string
    diverse_garland = ""
    # Loop through the lamps in the garland
    for i in range(n):
        # If the current lamp is not the same as the previous lamp
        if i == 0 or s[i] != s[i-1]:
            # Add the current lamp to the diverse garland
            diverse_garland += s[i]
        # If the current lamp is the same as the previous lamp
        else:
            # Increment the number of recolors
            recolors += 1
            # Add the current lamp to the diverse garland
            diverse_garland += "R" if s[i] == "G" else "G"
    # Return the number of recolors and the diverse garland
    return recolors, diverse_garland

