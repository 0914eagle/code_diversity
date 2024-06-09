
def solve(n, observations):
    # Initialize a dictionary to store the costume assignments
    costumes = {}

    # Iterate through the observations
    for observation in observations:
        # Extract the information from the observation
        i, l, r, x = observation

        # If the number of children with the orange pumpkin costume is even, assign the costume to child i
        if x == 0:
            costumes[i] = "orange pumpkin"

        # If the number of children with the orange pumpkin costume is odd, assign the costume to the children before and after child i
        elif x == 1:
            for j in range(i-l, i+r+1):
                costumes[j] = "orange pumpkin"

    # Return the number of ways to assign costumes consistent with the observations
    return len(set(costumes.values())) % (10**9 + 7)

