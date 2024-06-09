
def solve(N, P, bad_pairs):
    # Initialize a set to store the used ingredients
    used_ingredients = set()
    # Initialize a list to store the drinks
    drinks = []
    # Loop through the bad pairs of ingredients
    for a, b in bad_pairs:
        # If the ingredients are already used in a drink, remove them from the used ingredients set
        if a in used_ingredients or b in used_ingredients:
            used_ingredients.remove(a)
            used_ingredients.remove(b)
    # Loop through the remaining ingredients
    for i in range(1, N + 1):
        # If the ingredient is not used in any drink, add it to the used ingredients set
        if i not in used_ingredients:
            used_ingredients.add(i)
            # Add the ingredient to the list of drinks
            drinks.append(i)
    # Return the number of drinks
    return len(drinks)

