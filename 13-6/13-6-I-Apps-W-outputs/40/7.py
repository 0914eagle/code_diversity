
def get_two_pizzas(n, m, friends, pizzas):
    # Initialize the maximum number of pleased friends to 0
    max_pleased_friends = 0
    # Initialize the indices of the two pizzas to be returned
    pizza1 = 0
    pizza2 = 0
    
    # Iterate over each possible pair of pizzas
    for i in range(m):
        for j in range(i+1, m):
            # Initialize the number of pleased friends to 0
            pleased_friends = 0
            # Iterate over each friend and check if their favorite ingredients are in the current pair of pizzas
            for friend in friends:
                if all(ingredient in pizzas[i] for ingredient in friend):
                    pleased_friends += 1
            # If the current pair of pizzas pleases more friends than the previous pair, update the maximum number of pleased friends and the indices of the pizzas
            if pleased_friends > max_pleased_friends:
                max_pleased_friends = pleased_friends
                pizza1 = i
                pizza2 = j
    
    # Return the indices of the two pizzas that please the maximum number of friends
    return pizza1, pizza2

