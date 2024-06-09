
def get_diverse_garland(n, s):
    # Initialize the number of recolors to 0
    recolors = 0
    # Initialize the diverse garland as an empty string
    diverse_garland = ""
    # Iterate through the initial garland
    for i in range(n):
        # If the current lamp is red and the next lamp is also red, recolor the next lamp to green
        if s[i] == "R" and (i == n-1 or s[i+1] == "R"):
            recolors += 1
            diverse_garland += "G"
        # If the current lamp is green and the next lamp is also green, recolor the next lamp to blue
        elif s[i] == "G" and (i == n-1 or s[i+1] == "G"):
            recolors += 1
            diverse_garland += "B"
        # If the current lamp is blue and the next lamp is also blue, recolor the next lamp to red
        elif s[i] == "B" and (i == n-1 or s[i+1] == "B"):
            recolors += 1
            diverse_garland += "R"
        # If the current lamp is not red, green or blue, it is already diverse, so add it to the diverse garland
        else:
            diverse_garland += s[i]
    # Return the number of recolors and the diverse garland
    return recolors, diverse_garland

