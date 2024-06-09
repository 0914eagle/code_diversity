
def solve(s):
    # Initialize a dictionary to count the number of dead bulbs for each color
    dead_bulbs = {"R": 0, "B": 0, "Y": 0, "G": 0}

    # Iterate through the string and count the number of dead bulbs for each color
    for i in range(len(s)):
        if s[i] == "!":
            dead_bulbs[s[i-1]] += 1

    # Return the number of dead bulbs for each color
    return dead_bulbs["R"], dead_bulbs["B"], dead_bulbs["Y"], dead_bulbs["G"]

