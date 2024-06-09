
def get_pizzas(n, m, friends, pizzas):
    # Initialize the maximum number of pleased friends to 0
    max_pleased = 0
    # Initialize the indices of the two pizzas to be returned
    pizza1 = 0
    pizza2 = 0
    
    # Iterate over each possible pair of pizzas
    for i in range(m):
        for j in range(i+1, m):
            # Get the indices of the ingredients in the current pair of pizzas
            ingredients1 = pizzas[i]["ingredients"]
            ingredients2 = pizzas[j]["ingredients"]
            # Initialize the number of pleased friends to 0
            pleased = 0
            # Iterate over each friend and check if their favorite ingredients are in the current pair of pizzas
            for friend in friends:
                if set(ingredients1).intersection(friend["favorite"]):
                    pleased += 1
                if set(ingredients2).intersection(friend["favorite"]):
                    pleased += 1
            # If the current pair of pizzas pleased more friends than the previous pair, update the maximum number of pleased friends and the indices of the two pizzas
            if pleased > max_pleased:
                max_pleased = pleased
                pizza1 = i
                pizza2 = j
    
    # Return the indices of the two pizzas that pleased the maximum number of friends
    return [pizza1, pizza2]

