
def get_pizza_indices(n, m, friends, pizzas):
    # Initialize variables
    pleased_friends = 0
    total_price = 0
    chosen_pizzas = []

    # Iterate over all possible pairs of pizzas
    for i in range(m):
        for j in range(i+1, m):
            # Check if the pizzas include at least one favorite ingredient of each friend
            for friend in friends:
                if not any(ingredient in pizzas[i] for ingredient in friend):
                    break
            else:
                # If all friends are pleased, increment the number of pleased friends and calculate the total price
                pleased_friends += 1
                total_price += pizzas[i]['price'] + pizzas[j]['price']
                chosen_pizzas.append(i)
                chosen_pizzas.append(j)

    # Return the indices of the chosen pizzas that please the maximum number of friends and have the minimum total price
    return pleased_friends, total_price, chosen_pizzas

