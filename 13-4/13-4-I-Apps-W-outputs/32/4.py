
def get_pizzas(n, m, friends, pizzas):
    # Initialize the maximum number of pleased friends to 0
    max_pleased = 0
    # Initialize the indices of the two pizzas to be returned
    pizza1 = 0
    pizza2 = 0
    
    # Iterate over each pizza
    for i in range(m):
        # Get the price and ingredients of the current pizza
        price, ingredients = pizzas[i]
        # Initialize the number of pleased friends to 0
        pleased = 0
        # Iterate over each friend
        for j in range(n):
            # Get the favorite ingredients of the current friend
            favorite_ingredients = friends[j]
            # Check if the current pizza contains at least one of the friend's favorite ingredients
            if any(ingredient in ingredients for ingredient in favorite_ingredients):
                # Increment the number of pleased friends
                pleased += 1
        # Check if the current pizza pleased more friends than the maximum number of pleased friends
        if pleased > max_pleased:
            # Update the maximum number of pleased friends
            max_pleased = pleased
            # Update the indices of the two pizzas to be returned
            pizza1 = i
            pizza2 = i
    
    # Return the indices of the two pizzas
    return pizza1, pizza2

