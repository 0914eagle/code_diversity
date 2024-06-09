
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
    for perm in itertools.permutations(range(1, types + 1)):
        # Initialize a list to store the number of Pokemons of each type after evolution
        evolved_type_counts = [0] * (types + 1)
        
        # Iterate over the gyms and evolve the Pokemons according to the current plan
        for gym in gyms:
            for pokemon in gym:
                evolved_type_counts[perm[pokemon]] += 1
        
        # Check if the number of Pokemons of each type is the same before and after evolution
        if type_counts == evolved_type_counts:
            evolution_plans.append(perm)
    
    return len(evolution_plans)

def main():
    n, types = map(int, input().split())
    gyms = []
    for i in range(n):
        gym = list(map(int, input().split()))
        gyms.append(gym[1:])
    print(count_evolution_plans(gyms, types))

if __name__ == "__main__":
    main()

