
import itertools

def count_evolution_plans(gyms, types):
    # Initialize a list to store the number of Pokemons of each type
    type_counts = [0] * (types + 1)
    
    # Iterate over the gyms and count the number of Pokemons of each type
    for gym in gyms:
        for pokemon in gym:
            type_counts[pokemon] += 1
    
    # Use itertools.permutations to generate all possible evolution plans
    evolution_plans = itertools.permutations(range(1, types + 1))
    
    # Initialize a set to store the distinct evolution plans
    distinct_plans = set()
    
    # Iterate over the evolution plans and check if they satisfy the protocol
    for plan in evolution_plans:
        # Initialize a list to store the number of Pokemons of each type after evolution
        evolved_type_counts = [0] * (types + 1)
        
        # Iterate over the gyms and count the number of Pokemons of each type after evolution
        for gym in gyms:
            for pokemon in gym:
                evolved_type_counts[plan[pokemon]] += 1
        
        # Check if the number of Pokemons of each type is the same before and after evolution
        if type_counts == evolved_type_counts:
            distinct_plans.add(plan)
    
    return len(distinct_plans)

def main():
    gyms, types = map(int, input().split())
    gyms = [list(map(int, input().split())) for _ in range(gyms)]
    print(count_evolution_plans(gyms, types))

if __name__ == "__main__":
    main()

