
def solve(N, P, bad_pairs):
    # Initialize a set to store the used ingredients
    used_ingredients = set()
    # Initialize a list to store the drinks
    drinks = []
    # Loop through each bad pair of ingredients
    for a, b in bad_pairs:
        # If both ingredients are already used, remove them from the used ingredients set
        if a in used_ingredients and b in used_ingredients:
            used_ingredients.remove(a)
            used_ingredients.remove(b)
    # Loop through each ingredient
    for i in range(1, N + 1):
        # If the ingredient is not used, add it to the used ingredients set
        if i not in used_ingredients:
            # Add the ingredient to the drinks list
            drinks.append(i)
            # Add the ingredient to the used ingredients set
            used_ingredients.add(i)
    # Return the number of drinks
    return len(drinks)

