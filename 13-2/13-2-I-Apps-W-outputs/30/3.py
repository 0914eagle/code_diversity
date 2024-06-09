
def solve(recipes):
    # Initialize a set to store the ingredients used
    ingredients_used = set()
    # Initialize a counter for the number of recipes concocted
    num_concocted = 0

    for recipe in recipes:
        # Check if all ingredients in the recipe are available
        if all(ingredient in ingredients_used for ingredient in recipe[1:]):
            # Add the ingredients in the recipe to the set of used ingredients
            ingredients_used.update(recipe[1:])
            # Increment the counter for the number of recipes concocted
            num_concocted += 1

    return num_concocted

