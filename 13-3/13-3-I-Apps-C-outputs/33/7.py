
def solve(n, m, plants):
    # Sort the plants by their position
    plants.sort(key=lambda x: x[1])

    # Initialize the number of replants to 0
    replants = 0

    # Iterate through the plants
    for i in range(n):
        # Check if the current plant is not in the correct section
        if plants[i][0] != i + 1:
            # Increment the number of replants
            replants += 1

    # Return the number of replants
    return replants

