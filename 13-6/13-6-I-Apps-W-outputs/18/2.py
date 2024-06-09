
def solve(N, V, C):
    # Initialize the maximum total happiness as 0
    max_happiness = 0
    # Loop through each prime number from 2 to N
    for p in range(2, N+1):
        # If the prime number is not in the list of costs, skip it
        if p not in C:
            continue
        # Calculate the happiness increase for each Pokenom
        happiness_increase = sum([V[i] for i in range(N) if i % p == 0])
        # Calculate the happiness decrease for each Pokenom
        happiness_decrease = sum([C[p] * (i // p) ** 2 for i in range(N) if i % p == 0])
        # Calculate the total happiness for this prime number
        total_happiness = happiness_increase - happiness_decrease
        # Update the maximum total happiness if necessary
        max_happiness = max(max_happiness, total_happiness)
    # Return the maximum total happiness
    return max_happiness

