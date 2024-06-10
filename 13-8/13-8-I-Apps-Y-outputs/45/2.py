
def get_diverse_garland(n, s):
    # Initialize variables
    recolored_lamps = 0
    diverse_garland = []
    
    # Iterate through the garland
    for i in range(n):
        # If the current lamp is not the same as the previous lamp
        if i == 0 or s[i] != s[i-1]:
            # Add the current lamp to the diverse garland
            diverse_garland.append(s[i])
        # If the current lamp is the same as the previous lamp
        else:
            # Recolor the current lamp and add it to the diverse garland
            diverse_garland.append(get_recolored_lamps(s[i]))
            recolored_lamps += 1
    
    # Return the number of recolored lamps and the diverse garland
    return recolored_lamps, "".join(diverse_garland)

def get_recolored_lamps(color):
    # If the current lamp is red
    if color == "R":
        # Recolor it to green
        return "G"
    # If the current lamp is green
    elif color == "G":
        # Recolor it to blue
        return "B"
    # If the current lamp is blue
    else:
        # Recolor it to red
        return "R"

if __name__ == '__main__':
    n = int(input())
    s = input()
    recolored_lamps, diverse_garland = get_diverse_garland(n, s)
    print(recolored_lamps)
    print(diverse_garland)

