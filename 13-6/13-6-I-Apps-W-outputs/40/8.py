
def get_pizza_indices(n, m, friends, pizzas):
    # Initialize variables
    pleased_friends = 0
    total_price = 0
    chosen_pizzas = []

    # Iterate over all possible pairs of pizzas
    for i in range(m):
        for j in range(i+1, m):
            # Check if the current pair of pizzas pleases at least n friends
            current_pleased_friends = 0
            for friend in friends:
                if is_pizza_pleasing(friend, pizzas[i], pizzas[j]):
                    current_pleased_friends += 1
            if current_pleased_friends >= n:
                # Check if the current pair of pizzas is better than the previous one
                if current_pleased_friends > pleased_friends or (current_pleased_friends == pleased_friends and total_price > pizzas[i] + pizzas[j]):
                    pleased_friends = current_pleased_friends
                    total_price = pizzas[i] + pizzas[j]
                    chosen_pizzas = [i, j]

    return chosen_pizzas

def is_pizza_pleasing(friend, pizza1, pizza2):
    # Check if at least one of the friend's favorite ingredients is in at least one of the pizzas
    for ingredient in friend:
        if ingredient in pizza1 or ingredient in pizza2:
            return True
    return False

