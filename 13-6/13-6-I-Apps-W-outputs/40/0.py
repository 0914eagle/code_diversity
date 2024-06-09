
def get_two_pizzas(n, m, friends, pizzas):
    # Initialize the maximum number of pleased friends to 0
    max_pleased = 0
    # Initialize the indices of the two pizzas to choose from
    j1, j2 = 0, 0
    
    # Iterate over each pizza
    for j in range(m):
        # Initialize the number of pleased friends to 0
        pleased = 0
        # Iterate over each friend
        for i in range(n):
            # Check if the current pizza contains at least one of the friend's favorite ingredients
            if any(ingredient in pizzas[j] for ingredient in friends[i]):
                # Increment the number of pleased friends
                pleased += 1
        # Check if the current pizza pleases more friends than the previous pizzas
        if pleased > max_pleased:
            # Update the indices of the two pizzas to choose from
            j1, j2 = j, j1
            # Update the maximum number of pleased friends
            max_pleased = pleased
    
    # Return the indices of the two pizzas to choose from
    return j1, j2

