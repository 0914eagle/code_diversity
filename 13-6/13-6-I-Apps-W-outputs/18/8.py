
def solve(N, V, C):
    # Initialize the maximum total happiness as 0
    max_happiness = 0
    # Loop through each possible combination of ingredients
    for i in range(1, N+1):
        # Calculate the happiness of Bash and the Pokenoms for this combination
        happiness = calculate_happiness(i, N, V, C)
        # Update the maximum total happiness if this combination leads to more happiness
        max_happiness = max(max_happiness, happiness)
    # Return the maximum total happiness
    return max_happiness

def calculate_happiness(i, N, V, C):
    # Initialize the happiness of Bash and the Pokenoms as 0
    happiness = 0
    # Loop through each prime factor of i
    for p in range(2, int(N**0.5) + 1):
        # If p is a prime factor of i
        if i % p == 0:
            # Calculate the amount of ingredient p needed for the ith cake
            amount = 1
            # Loop through each prime factor of p
            while i % p == 0:
                i //= p
                amount *= p
            # Add the happiness decrease due to buying amount grams of ingredient p
            happiness -= amount**2 * C[p]
    # Add the happiness increase due to having enough ingredients for the ith cake
    happiness += V[i]
    # Return the total happiness
    return happiness

