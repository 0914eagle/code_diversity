
def solve(N, P, bad_pairs):
    # Initialize a set to store the available ingredients
    available_ingredients = set(range(1, N + 1))
    # Initialize a set to store the used ingredients
    used_ingredients = set()
    # Initialize a list to store the drinks
    drinks = []
    # Loop through each bad pair of ingredients
    for a, b in bad_pairs:
        # If both ingredients are available, remove them from the available ingredients set
        if a in available_ingredients and b in available_ingredients:
            available_ingredients.remove(a)
            available_ingredients.remove(b)
    # Loop through each ingredient
    for i in range(1, N + 1):
        # If the ingredient is available, add it to the used ingredients set
        if i in available_ingredients:
            used_ingredients.add(i)
        # If the ingredient is not available, add the used ingredients set to the drinks list
        else:
            drinks.append(used_ingredients.copy())
            used_ingredients.clear()
    # Return the number of nights Pia can construct a different set of drinks
    return len(drinks) % (10**9 + 7)

