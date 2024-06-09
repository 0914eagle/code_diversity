
def get_pizza_indices(n, m, friends, pizzas):
    # Initialize variables
    pleased_friends = 0
    total_price = 0
    chosen_pizzas = []

    # Iterate through each pizza
    for i in range(m):
        # Check if the pizza has at least one favorite ingredient of each friend
        for friend in friends:
            for ingredient in friend:
                if ingredient in pizzas[i]:
                    pleased_friends += 1
                    break

        # If the pizza has at least one favorite ingredient of each friend, add it to the chosen pizzas
        if pleased_friends == n:
            chosen_pizzas.append(i)
            total_price += pizzas[i][0]
            break

        # Reset the pleased friends count
        pleased_friends = 0

    # Return the indices of the chosen pizzas and their total price
    return chosen_pizzas, total_price

