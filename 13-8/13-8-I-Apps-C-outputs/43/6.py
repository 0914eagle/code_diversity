
def solve(N, P, bad_pairs):
    # Initialize a set to store the used ingredients
    used_ingredients = set()
    # Initialize a list to store the drinks
    drinks = []
    # Loop through the bad pairs of ingredients
    for a, b in bad_pairs:
        # If both ingredients are already used, skip this pair
        if a in used_ingredients and b in used_ingredients:
            continue
        # If either ingredient is already used, skip this pair
        if a in used_ingredients or b in used_ingredients:
            continue
        # Add both ingredients to the used ingredients set
        used_ingredients.add(a)
        used_ingredients.add(b)
    # Loop through the remaining ingredients
    for i in range(1, N + 1):
        # If the ingredient is not used, add it to the list of drinks
        if i not in used_ingredients:
            drinks.append(i)
    # Return the number of drinks modulo 10^9 + 7
    return len(drinks) % (10**9 + 7)

