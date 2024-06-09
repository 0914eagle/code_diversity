
def solve(n, observations):
    # Initialize a dictionary to store the parity of the costume for each child
    costumes = {}

    # Iterate through the observations
    for observation in observations:
        # Extract the information from the observation
        i, l, r, x = observation

        # If the number of children with the orange pumpkin costume is even, set the parity of the current child to 0
        if x == 0:
            costumes[i] = 0

        # If the number of children with the orange pumpkin costume is odd, set the parity of the current child to 1
        elif x == 1:
            costumes[i] = 1

        # If the current child has already been assigned a parity, check if the current observation is consistent with the assigned parity
        if i in costumes and costumes[i] != x:
            return 0

    # If all observations are consistent, return the number of ways to assign costumes to the children
    return 1

