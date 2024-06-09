
def solve(N, V, C):
    # Initialize the maximum total happiness as 0
    max_happiness = 0
    # Loop through each possible combination of ingredients
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                # Calculate the total happiness for this combination of ingredients
                total_happiness = V[i] + V[j] + V[k]
                # Check if the total happiness is greater than the current maximum
                if total_happiness > max_happiness:
                    # If so, update the maximum total happiness
                    max_happiness = total_happiness
    # Return the maximum total happiness
    return max_happiness

