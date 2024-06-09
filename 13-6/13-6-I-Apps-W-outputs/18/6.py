
def solve(N, V, C):
    # Initialize the maximum total happiness as 0
    max_happiness = 0
    # Loop through each prime number from 2 to N
    for i in range(2, N+1):
        # If the prime number is not in the list of C, continue to the next iteration
        if i not in C:
            continue
        # Calculate the happiness decrease for buying 1 gram of the current prime number
        happiness_decrease = -1 * C[i]
        # Calculate the happiness increase for the Pokenoms that can be fed with the current cake
        happiness_increase = sum(V[j] for j in range(1, N+1) if i in prime_factors(j))
        # Calculate the total happiness for the current combination of ingredients
        total_happiness = happiness_increase + happiness_decrease
        # Update the maximum total happiness if the current total happiness is higher
        max_happiness = max(max_happiness, total_happiness)
    # Return the maximum total happiness
    return max_happiness

# Function to calculate the prime factors of a number
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

