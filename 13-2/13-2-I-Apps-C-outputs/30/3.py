
def solve(N, P, bad_pairs):
    # Initialize a set to store the used ingredients
    used_ingredients = set()
    # Initialize a list to store the drinks
    drinks = []
    # Loop through the bad pairs of ingredients
    for a, b in bad_pairs:
        # If the ingredients are not already used, add them to the used ingredients set
        if a not in used_ingredients and b not in used_ingredients:
            used_ingredients.add(a)
            used_ingredients.add(b)
    # Loop through the remaining ingredients
    for i in range(1, N + 1):
        # If the ingredient is not already used, add it to the drink
        if i not in used_ingredients:
            drinks.append(i)
    # Return the number of drinks
    return len(drinks)

