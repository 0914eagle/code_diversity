
def solve(N, V, C):
    # Initialize the maximum total happiness as 0
    max_happiness = 0
    # Loop through each possible amount of ingredients
    for i in range(1, N+1):
        # Calculate the happiness of Bash and the Pokenoms with the current amount of ingredients
        happiness = calculate_happiness(i, V, C)
        # Update the maximum total happiness if the current happiness is greater than the previous maximum
        max_happiness = max(max_happiness, happiness)
    # Return the maximum total happiness
    return max_happiness

def calculate_happiness(i, V, C):
    # Initialize the happiness of Bash and the Pokenoms as 0
    happiness = 0
    # Loop through each prime number up to the current amount of ingredients
    for p in range(2, i+1):
        # If the prime number is a factor of the current amount of ingredients
        if i % p == 0:
            # Add the happiness of Bash and the Pokenoms from the current ingredient to the total happiness
            happiness += V[p-1] + C[p-1] * (i // p) ** 2
    # Return the total happiness
    return happiness

