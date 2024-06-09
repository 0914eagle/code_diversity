
import itertools

def count_evolution_plans(n, m, gyms):
    # Initialize a list to store the number of Pokemons of each type
    types = [0] * (m + 1)
    
    # Iterate over the gyms and count the number of Pokemons of each type
    for gym in gyms:
        for pokemon in gym:
            types[pokemon] += 1
    
    # Initialize a list to store the evolution plans
    plans = []
    
    # Iterate over the permutations of the Pokemon types
    for perm in itertools.permutations(range(1, m + 1)):
        # Initialize a list to store the number of Pokemons of each type after evolving
        evolved_types = [0] * (m + 1)
        
        # Iterate over the gyms and evolve the Pokemons according to the current plan
        for gym in gyms:
            for pokemon in gym:
                evolved_types[perm[pokemon]] += 1
        
        # Check if the number of Pokemons of each type is the same before and after evolving
        if types == evolved_types:
            plans.append(perm)
    
    return len(plans)

def main():
    n, m = map(int, input().split())
    gyms = []
    for i in range(n):
        gym = list(map(int, input().split()))
        gyms.append(gym[1:])
    print(count_evolution_plans(n, m, gyms))

if __name__ == "__main__":
    main()

