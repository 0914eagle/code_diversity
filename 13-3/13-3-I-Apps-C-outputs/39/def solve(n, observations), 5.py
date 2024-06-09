
def solve(n, observations):
    # Initialize a dictionary to store the parity of the costume for each child
    costumes = {}

    # Iterate through the observations
    for observation in observations:
        # Extract the indices of the children in the observation
        i, l, r, x = observation

        # If the number of children in the observation is odd, set the parity of the costume for child i to 1 (odd)
        if l + r + 1 % 2 == 1:
            costumes[i] = 1

        # If the number of children in the observation is even, set the parity of the costume for child i to 0 (even)
        else:
            costumes[i] = 0

    # Initialize a variable to store the number of ways to assign costumes
    num_ways = 1

    # Iterate through the children
    for i in range(n):
        # If the parity of the costume for child i is not set, set it to the opposite of the parity of the costume for the previous child
        if costumes[i] == None:
            costumes[i] = 1 - costumes[(i - 1) % n]

        # Update the number of ways to assign costumes based on the parity of the costume for child i
        num_ways *= 2

    # Return the number of ways to assign costumes modulo 10^9 + 7
    return num_ways % (10**9 + 7)

