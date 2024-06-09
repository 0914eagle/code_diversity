
def solve(N, P, bad_pairs):
    # Initialize a set to store the indices of the ingredients that have been used
    used_ingredients = set()
    # Initialize a list to store the indices of the ingredients for each drink
    drink_ingredients = []
    # Initialize a variable to store the number of drinks made
    num_drinks = 0
    # Loop through each bad pair of ingredients
    for a, b in bad_pairs:
        # If both ingredients have already been used, skip this pair
        if a in used_ingredients and b in used_ingredients:
            continue
        # If one of the ingredients has already been used, add the other ingredient to the set of used ingredients
        elif a in used_ingredients:
            used_ingredients.add(b)
        elif b in used_ingredients:
            used_ingredients.add(a)
        # If neither ingredient has been used, add both to the set of used ingredients
        else:
            used_ingredients.add(a)
            used_ingredients.add(b)
    # Loop through each ingredient
    for i in range(1, N + 1):
        # If the ingredient has not been used, add it to the list of ingredients for the current drink
        if i not in used_ingredients:
            drink_ingredients.append(i)
    # Increment the number of drinks made
    num_drinks += 1
    # Return the number of drinks made
    return num_drinks % 1000000007

