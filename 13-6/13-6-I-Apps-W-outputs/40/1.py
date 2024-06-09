
def solve(n, m, friends, pizzas):
    # Initialize the maximum number of satisfied friends to 0
    max_satisfied = 0
    # Initialize the indices of the two pizzas to be returned
    pizza1 = 0
    pizza2 = 0
    
    # Iterate over each possible pair of pizzas
    for i in range(m):
        for j in range(i+1, m):
            # Initialize the number of satisfied friends to 0
            satisfied = 0
            # Iterate over each friend and check if their favorite ingredients are in the current pair of pizzas
            for friend in friends:
                if set(friend).intersection(pizzas[i]) or set(friend).intersection(pizzas[j]):
                    satisfied += 1
            # If the current pair of pizzas satisfies more friends than the previous maximum, update the maximum and the indices of the pizzas
            if satisfied > max_satisfied:
                max_satisfied = satisfied
                pizza1 = i
                pizza2 = j
    
    return [pizza1, pizza2]

