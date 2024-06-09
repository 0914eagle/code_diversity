
def solve(n, m, windows):
    # Initialize a set to store the flats with lights on
    lights_on = set()

    # Iterate through each floor
    for i in range(n):
        # Iterate through each window on the current floor
        for j in range(m):
            # If the window has lights on, add the corresponding flat to the set
            if windows[i][j] == "1":
                lights_on.add(j)

    # Return the number of flats with lights on
    return len(lights_on)

