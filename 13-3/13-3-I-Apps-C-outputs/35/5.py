
import itertools

def count_evolution_plans(gyms, types):
    # Initialize a counter for the number of distinct evolution plans
    count = 0
    
    # Iterate over all possible evolution plans
    for plan in itertools.permutations(types):
        # Check if the plan satisfies the protocol
        if satisfies_protocol(gyms, plan):
            # Increment the counter
            count += 1
    
    # Return the counter modulo 10^9 + 7
    return count % 1000000007

def satisfies_protocol(gyms, plan):
    # Initialize a dictionary to store the number of Pokemons of each type before evolution
    before = {}
    for i in range(1, len(plan) + 1):
        before[i] = 0
    
    # Initialize a dictionary to store the number of Pokemons of each type after evolution
    after = {}
    for i in range(1, len(plan) + 1):
        after[i] = 0
    
    # Iterate over all gyms
    for gym in gyms:
        # Iterate over all Pokemons in the gym
        for pokemon in gym:
            # Get the type of the Pokemon before evolution
            before_type = pokemon[0]
            # Get the type of the Pokemon after evolution
            after_type = plan[before_type - 1]
            # Increment the number of Pokemons of the before type
            before[before_type] += 1
            # Increment the number of Pokemons of the after type
            after[after_type] += 1
    
    # Check if the number of Pokemons of each type is the same before and after evolution
    for i in range(1, len(plan) + 1):
        if before[i] != after[i]:
            return False
    
    # If all Pokemons have the same number of types before and after evolution, return True
    return True

def main():
    # Read the input
    n, m = map(int, input().split())
    gyms = []
    for i in range(n):
        gym = list(map(int, input().split()))
        gyms.append(gym[1:])
    
    # Call the count_evolution_plans function and print the result
    print(count_evolution_plans(gyms, range(1, m + 1)))

if __name__ == '__main__':
    main()

