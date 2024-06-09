
def solve(n, observations):
    # Initialize a dictionary to store the parity of the costume for each child
    costumes = {}

    # Iterate through the observations
    for observation in observations:
        # Extract the information from the observation
        i, l, r, x = observation

        # If the child is wearing the orange pumpkin costume, update the parity of the costume for the child and its neighbors
        if x == 0:
            costumes[i] = "orange"
            for j in range(i-l, i+r+1):
                costumes[j%n] = "orange"

        # If the child is wearing the black bat costume, update the parity of the costume for the child and its neighbors
        else:
            costumes[i] = "black"
            for j in range(i-l, i+r+1):
                costumes[j%n] = "black"

    # Initialize a variable to store the number of ways to assign costumes
    num_ways = 1

    # Iterate through the children
    for i in range(n):
        # If the parity of the costume for the child is not determined, return 0
        if costumes[i] == None:
            return 0

        # If the parity of the costume for the child is determined, update the number of ways to assign costumes
        else:
            num_ways *= 2

    # Return the number of ways to assign costumes modulo 10^9 + 7
    return num_ways % 1000000007

