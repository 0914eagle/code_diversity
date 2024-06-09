
def count_evolution_plans(n, m, gyms):
    # Initialize a list to store the number of Pokemons of each type
    num_pokemons = [0] * (m + 1)
    
    # Iterate over the gyms and count the number of Pokemons of each type
    for gym in gyms:
        for pokemon in gym:
            num_pokemons[pokemon] += 1
    
    # Initialize a list to store the number of evolution plans for each type
    num_plans = [0] * (m + 1)
    
    # Iterate over the types and count the number of evolution plans for each type
    for i in range(1, m + 1):
        # If the number of Pokemons of this type is 0, then there are no evolution plans for this type
        if num_pokemons[i] == 0:
            continue
        
        # If the number of Pokemons of this type is 1, then there is only one evolution plan for this type
        if num_pokemons[i] == 1:
            num_plans[i] = 1
            continue
        
        # If the number of Pokemons of this type is greater than 1, then there are num_pokemons[i]! evolution plans for this type
        num_plans[i] = math.factorial(num_pokemons[i])
    
    # Return the product of the number of evolution plans for each type
    return math.prod(num_plans) % (10**9 + 7)

