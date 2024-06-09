
def get_concocted_recipes(recipes):
    # Initialize a set to keep track of the ingredients used
    ingredients_used = set()
    # Initialize a list to store the concocted recipes
    concocted_recipes = []

    for recipe in recipes:
        # Check if all the ingredients in the recipe are available
        if all(ingredient in ingredients_used for ingredient in recipe[1:]):
            # Add the ingredients used in this recipe to the set
            ingredients_used.update(recipe[1:])
            # Add the recipe to the list of concocted recipes
            concocted_recipes.append(recipe)

    return len(concocted_recipes)

