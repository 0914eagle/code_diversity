
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
    for f in permutations(range(1, m + 1)):
        # Initialize a list to store the number of Pokemons of each type after evolution
        types_after = [0] * (m + 1)

        # Iterate over the gyms and count the number of Pokemons of each type after evolution
        for gym in gyms:
            for pokemon in gym:
                types_after[f[pokemon]] += 1

        # Check if the number of Pokemons of each type is the same before and after evolution
        if types == types_after:
            plans.append(f)

    return len(plans) % (10**9 + 7)

