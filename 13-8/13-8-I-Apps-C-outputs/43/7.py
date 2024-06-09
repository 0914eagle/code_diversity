
def solve(N, P, bad_pairs):
    # Initialize a set to store the used ingredients
    used_ingredients = set()
    # Initialize a list to store the drinks
    drinks = []
    # Loop through the bad pairs of ingredients
    for a, b in bad_pairs:
        # If both ingredients are already used, they cannot be used together
        if a in used_ingredients and b in used_ingredients:
            return 0
    # Loop through the ingredients
    for i in range(1, N + 1):
        # If the ingredient is not used, use it
        if i not in used_ingredients:
            # Add the ingredient to the used ingredients set
            used_ingredients.add(i)
            # Add the ingredient to the drinks list
            drinks.append(i)
            # If all ingredients are used, return the number of drinks
            if len(used_ingredients) == N:
                return len(drinks)
    # If all ingredients are used and not all drinks are made, return 0
    return 0

