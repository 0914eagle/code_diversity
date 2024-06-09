
def get_two_pizzas(n, m, friends, pizzas):
    # Initialize the maximum number of pleased friends to 0
    max_pleased = 0
    # Initialize the indices of the two pizzas to -1
    pizza1 = -1
    pizza2 = -1
    
    # Iterate over each pizza
    for i in range(m):
        # Initialize the number of pleased friends to 0
        pleased = 0
        # Iterate over each friend
        for j in range(n):
            # Check if the friend's favorite ingredients are in the current pizza
            if set(friends[j]).issubset(set(pizzas[i])):
                # Increment the number of pleased friends
                pleased += 1
        # Check if the current pizza pleases more friends than the previous pizzas
        if pleased > max_pleased:
            # Update the maximum number of pleased friends
            max_pleased = pleased
            # Update the indices of the two pizzas
            pizza1 = i
            pizza2 = i
    
    # Return the indices of the two pizzas
    return pizza1, pizza2

