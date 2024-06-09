
def num_drinks(num_ingredients, bad_pairs):
    # Initialize a set to store the used ingredients
    used_ingredients = set()
    # Initialize a list to store the drinks
    drinks = []
    # Iterate through the bad pairs
    for pair in bad_pairs:
        # If the first ingredient of the pair is not used, add it to the used ingredients set
        if pair[0] not in used_ingredients:
            used_ingredients.add(pair[0])
        # If the second ingredient of the pair is not used, add it to the used ingredients set
        if pair[1] not in used_ingredients:
            used_ingredients.add(pair[1])
    # Iterate through the remaining ingredients
    for ingredient in range(1, num_ingredients + 1):
        # If the ingredient is not used, add it to the drinks list
        if ingredient not in used_ingredients:
            drinks.append(ingredient)
    # Return the number of drinks
    return len(drinks)

