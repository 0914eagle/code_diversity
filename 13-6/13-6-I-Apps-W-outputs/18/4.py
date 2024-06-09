
def solve(N, V, C):
    # Initialize the maximum total happiness as 0
    max_happiness = 0
    # Loop through each prime number from 2 to N
    for p in range(2, N+1):
        # If the prime number is not in the list of costs, skip it
        if p not in C:
            continue
        # Find the exponent of the prime number in the recipe
        exponent = 0
        while p ** (exponent+1) <= N:
            exponent += 1
        # Calculate the amount of ingredient needed for the cake
        amount = p ** exponent
        # Calculate the cost of the ingredient
        cost = amount * C[p]
        # Calculate the happiness increase for Bash and the Pokenoms
        happiness = amount * V[p] - cost
        # If the happiness increase is positive, update the maximum total happiness
        if happiness > 0:
            max_happiness = max(max_happiness, happiness)
    # Return the maximum total happiness
    return max_happiness

