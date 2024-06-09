
def solve(N, P, bad_pairs):
    # Initialize a set to store the available ingredients
    available_ingredients = set(range(1, N + 1))
    # Initialize a set to store the used ingredients
    used_ingredients = set()
    # Initialize a list to store the drinks
    drinks = []
    # Initialize a variable to store the number of nights
    nights = 0

    while len(available_ingredients) > 0:
        # Choose a random ingredient from the available ingredients
        ingredient = random.choice(list(available_ingredients))
        # Add the ingredient to the used ingredients set
        used_ingredients.add(ingredient)
        # Remove the ingredient from the available ingredients set
        available_ingredients.remove(ingredient)
        # Add the ingredient to the list of drinks
        drinks.append(ingredient)
        # Increment the number of nights
        nights += 1

        # Check if the current drink has any bad pairs with the previous drinks
        for drink in drinks:
            if (ingredient, drink) in bad_pairs or (drink, ingredient) in bad_pairs:
                # If a bad pair is found, remove the ingredient from the used ingredients set
                used_ingredients.remove(ingredient)
                # Remove the ingredient from the list of drinks
                drinks.pop()
                # Decrement the number of nights
                nights -= 1
                # Break out of the loop
                break

    # Return the number of nights modulo 10^9 + 7
    return nights % (10**9 + 7)

