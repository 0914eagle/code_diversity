
def get_pizza_indices(n, m, friends, pizzas):
    # Initialize variables
    pleased_friends = 0
    total_price = 0
    chosen_pizzas = []

    # Iterate over each pizza
    for i in range(m):
        # Check if the pizza has at least one favorite ingredient of each friend
        for friend in friends:
            for ingredient in friend:
                if ingredient in pizzas[i]:
                    break
            else:
                break
        else:
            # If the pizza has at least one favorite ingredient of each friend, increment the pleased friends count
            pleased_friends += 1
            # Add the pizza to the chosen pizzas list
            chosen_pizzas.append(i)
            # Add the pizza price to the total price
            total_price += pizzas[i][0]

        # If the pleased friends count is equal to the number of friends, break the loop
        if pleased_friends == n:
            break

    # Return the chosen pizzas indices and the total price
    return chosen_pizzas, total_price

