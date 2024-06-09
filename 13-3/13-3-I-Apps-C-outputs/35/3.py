
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
    # Initialize a dictionary to store the number of Pokemons of each type
    types = {}
    for i in range(1, len(plan) + 1):
        types[i] = 0
    
    # Iterate over all gyms
    for gym in gyms:
        # Iterate over all Pokemons in the gym
        for pokemon in gym:
            # Increment the number of Pokemons of the current type
            types[pokemon] += 1
    
    # Iterate over all types
    for type in types:
        # Check if the number of Pokemons of the current type is equal to the number of Pokemons of the corresponding type after evolving
        if types[type] != types[plan[type - 1]]:
            # Return False if the protocol is not satisfied
            return False
    
    # Return True if the protocol is satisfied
    return True

def main():
    # Read the input
    n, m = map(int, input().split())
    gyms = []
    for i in range(n):
        gyms.append(list(map(int, input().split())))
    
    # Call the count_evolution_plans function and print the result
    print(count_evolution_plans(gyms, range(1, m + 1)))

if __name__ == '__main__':
    main()

