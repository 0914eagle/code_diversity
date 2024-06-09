
def get_maximum_happiness(N, V, C):
    # Initialize the happiness of Bash and his Pokenoms to 0
    happiness = 0
    
    # Iterate through each Pokenom and check if it has enough ingredients for its cake
    for i in range(1, N+1):
        # Calculate the amount of ingredients needed for the ith cake
        ingredients_needed = 0
        for j in range(2, int(N**0.5) + 1):
            if i % j == 0:
                ingredients_needed += 1
        happiness += V[i-1]
    
    # Calculate the happiness decrease due to the cost of the ingredients
    for i in range(1, N+1):
        if C[i] != 0:
            happiness -= C[i] * (ingredients_needed ** 2)
    
    return happiness

