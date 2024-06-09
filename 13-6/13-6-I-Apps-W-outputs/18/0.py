
def get_max_happiness(N, V, C):
    # Initialize the happiness of Bash and his Pokenoms to 0
    happiness = 0
    
    # Iterate through each Pokenom and its corresponding cake
    for i in range(1, N+1):
        # Calculate the ingredients needed for the ith cake
        ingredients = []
        for j in range(2, int(N**0.5) + 1):
            if i % j == 0:
                ingredients.append(j)
        ingredients = list(set(ingredients))
        
        # Calculate the cost of buying the ingredients needed for the ith cake
        cost = 0
        for j in ingredients:
            cost += C[j-1] * j
        
        # Update the happiness of Bash and his Pokenoms
        happiness += V[i-1] - cost
    
    return happiness

