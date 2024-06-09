
import itertools

def count_evolution_plans(gyms, types):
    # Initialize a list to store the number of Pokemons of each type
    type_counts = [0] * (types + 1)
    
    # Iterate over the gyms and count the number of Pokemons of each type
    for gym in gyms:
        for pokemon in gym:
            type_counts[pokemon] += 1
    
    # Initialize a list to store the evolution plans
    evolution_plans = []
    
    # Iterate over the permutations of the types
    for permutation in itertools.permutations(range(1, types + 1)):
        # Initialize a list to store the number of Pokemons of each type after evolution
        evolved_type_counts = [0] * (types + 1)
        
        # Iterate over the gyms and evolve the Pokemons according to the current permutation
        for gym in gyms:
            for pokemon in gym:
                evolved_type_counts[permutation[pokemon]] += 1
        
        # Check if the number of Pokemons of each type is the same before and after evolution
        if type_counts == evolved_type_counts:
            evolution_plans.append(permutation)
    
    # Return the number of distinct evolution plans
    return len(set(frozenset(plan) for plan in evolution_plans)) % (10**9 + 7)


n, m = map(int, input().split())
gyms = []
for _ in range(n):
    gym = list(map(int, input().split()))
    gyms.append(gym[1:])

print(count_evolution_plans(gyms, m))

