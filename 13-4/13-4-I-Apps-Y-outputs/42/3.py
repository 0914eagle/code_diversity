
def get_diverse_garland(n, s):
    # Initialize the number of recolors to 0
    recolors = 0
    # Initialize the diverse garland as an empty string
    diverse_garland = ""
    # Iterate through the input garland
    for i in range(n):
        # If the current lamp is red and the previous lamp is not red, recolor it
        if s[i] == "R" and (i == 0 or s[i-1] != "R"):
            recolors += 1
            diverse_garland += "R"
        # If the current lamp is green and the previous lamp is not green, recolor it
        elif s[i] == "G" and (i == 0 or s[i-1] != "G"):
            recolors += 1
            diverse_garland += "G"
        # If the current lamp is blue and the previous lamp is not blue, recolor it
        elif s[i] == "B" and (i == 0 or s[i-1] != "B"):
            recolors += 1
            diverse_garland += "B"
        # If the current lamp is the same as the previous lamp, do not recolor it
        else:
            diverse_garland += s[i]
    # Return the number of recolors and the diverse garland
    return recolors, diverse_garland

