
def get_pizzas(n, m, friends, pizzas):
    # Initialize the maximum number of pleased friends to 0
    max_pleased = 0
    # Initialize the indices of the two pizzas to be returned
    pizza1 = 0
    pizza2 = 0
    
    # Iterate over each possible combination of two pizzas
    for i in range(m):
        for j in range(i+1, m):
            # Initialize the number of pleased friends to 0
            pleased = 0
            # Iterate over each friend and check if their favorite ingredients are in the current combination of pizzas
            for k in range(n):
                if set(friends[k]).intersection(set(pizzas[i])) and set(friends[k]).intersection(set(pizzas[j])):
                    pleased += 1
            # If the current combination of pizzas pleased more friends than the previous best combination, update the best combination
            if pleased > max_pleased:
                max_pleased = pleased
                pizza1 = i
                pizza2 = j
    
    # Return the indices of the two pizzas that pleased the maximum number of friends
    return pizza1, pizza2

