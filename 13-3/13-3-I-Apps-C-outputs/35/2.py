
def solve(n, m, gyms):
    # Initialize a list to store the number of Pokemons of each type
    types = [0] * (m + 1)

    # Iterate over the gyms and count the number of Pokemons of each type
    for gym in gyms:
        for pokemon in gym:
            types[pokemon] += 1

    # Initialize a list to store the possible evolution plans
    plans = []

    # Iterate over the possible evolution plans
    for plan in permutations(range(1, m + 1)):
        # Initialize a list to store the number of Pokemons of each type after evolving
        evolved_types = [0] * (m + 1)

        # Iterate over the gyms and count the number of Pokemons of each type after evolving
        for gym in gyms:
            for pokemon in gym:
                evolved_types[plan[pokemon]] += 1

        # Check if the number of Pokemons of each type is the same before and after evolving
        if types == evolved_types:
            plans.append(plan)

    return len(plans) % (10**9 + 7)

