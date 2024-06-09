
def get_diverse_garland(n, s):
    # Initialize the number of recolors to 0
    recolors = 0
    # Initialize the diverse garland as an empty string
    diverse_garland = ""
    # Iterate through the initial garland
    for i in range(n):
        # If the current lamp is red and the previous lamp is not red, recolor it
        if s[i] == "R" and (i == 0 or s[i-1] != "R"):
            diverse_garland += "R"
            recolors += 1
        # If the current lamp is green and the previous lamp is not green, recolor it
        elif s[i] == "G" and (i == 0 or s[i-1] != "G"):
            diverse_garland += "G"
            recolors += 1
        # If the current lamp is blue and the previous lamp is not blue, recolor it
        elif s[i] == "B" and (i == 0 or s[i-1] != "B"):
            diverse_garland += "B"
            recolors += 1
        # If the current lamp is the same as the previous lamp, do not recolor it
        else:
            diverse_garland += s[i]
    # Return the number of recolors and the diverse garland
    return recolors, diverse_garland

