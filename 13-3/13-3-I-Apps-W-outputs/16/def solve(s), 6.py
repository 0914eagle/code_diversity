
def solve(s):
    # Initialize a dictionary to store the count of each color
    color_count = {"R": 0, "B": 0, "Y": 0, "G": 0}

    # Iterate through the string and increment the count of each color
    for c in s:
        if c != "!":
            color_count[c] += 1

    # Return the count of each color
    return " ".join(str(color_count[c]) for c in "RBGY")

