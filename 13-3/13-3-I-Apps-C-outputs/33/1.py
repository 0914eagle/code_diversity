
def solve(n, m, plants):
    # Sort the plants by their position
    plants.sort(key=lambda x: x[1])

    # Initialize the minimum number of replants to 0
    min_replants = 0

    # Iterate through the plants
    for i in range(n):
        # Check if the current plant is not in the correct section
        if plants[i][0] != i + 1:
            # Increment the minimum number of replants
            min_replants += 1

    # Return the minimum number of replants
    return min_replants

