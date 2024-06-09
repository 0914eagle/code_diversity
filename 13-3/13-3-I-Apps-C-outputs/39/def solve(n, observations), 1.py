
def solve(n, observations):
    # Initialize a dictionary to store the parity of the costume for each child
    costumes = {}

    # Iterate through the observations
    for i, (l, r, x) in enumerate(observations):
        # Get the indices of the children before and after the current child
        before = (i - l) % n
        after = (i + r + 1) % n

        # If the current child is wearing the orange pumpkin costume, update the parity of the costume for the children before and after
        if x == 1:
            costumes[before] = 1 - costumes.get(before, 0)
            costumes[after] = 1 - costumes.get(after, 0)

    # Initialize a variable to store the number of ways to assign costumes
    num_ways = 1

    # Iterate through the children and update the number of ways to assign costumes based on the parity of the costume
    for i in range(n):
        if costumes.get(i, 0) == 1:
            num_ways *= 2
        else:
            num_ways *= 2 - costumes.get(i, 0)

    # Return the number of ways to assign costumes modulo 10^9 + 7
    return num_ways % (10**9 + 7)

