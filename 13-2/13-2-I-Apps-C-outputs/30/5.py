
def solve(N, P, bad_pairs):
    # Initialize a set to store the used ingredients
    used_ingredients = set()
    # Initialize a list to store the drinks
    drinks = []
    # Loop through each bad pair of ingredients
    for a, b in bad_pairs:
        # If both ingredients are already used, skip this pair
        if a in used_ingredients and b in used_ingredients:
            continue
        # If either ingredient is already used, add the other ingredient to the used ingredients set
        elif a in used_ingredients:
            used_ingredients.add(b)
        elif b in used_ingredients:
            used_ingredients.add(a)
        # If neither ingredient is used, add both to the used ingredients set
        else:
            used_ingredients.update([a, b])
    # Loop through each ingredient
    for i in range(1, N + 1):
        # If the ingredient is not used, add it to the list of drinks
        if i not in used_ingredients:
            drinks.append(i)
    # Return the number of drinks modulo 10^9 + 7
    return len(drinks) % (10**9 + 7)

