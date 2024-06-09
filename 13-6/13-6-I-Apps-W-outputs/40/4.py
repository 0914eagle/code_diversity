
def get_pizza_indices(n, m, friends, pizzas):
    # Initialize variables
    pleased_friends = 0
    total_price = 0
    chosen_pizzas = []

    # Iterate over all possible combinations of pizzas
    for i in range(m):
        for j in range(i+1, m):
            # Check if the current combination of pizzas pleases at least n friends
            current_pleased_friends = 0
            for friend in friends:
                if is_pleased(friend, pizzas[i], pizzas[j]):
                    current_pleased_friends += 1
            if current_pleased_friends >= n:
                # If the current combination pleases more friends than the previous one, update the variables
                if current_pleased_friends > pleased_friends:
                    pleased_friends = current_pleased_friends
                    total_price = pizzas[i]["price"] + pizzas[j]["price"]
                    chosen_pizzas = [i, j]

    return chosen_pizzas

def is_pleased(friend, pizza1, pizza2):
    # Check if the friend is pleased with at least one of the pizzas
    for ingredient in friend["favorite_ingredients"]:
        if ingredient in pizza1["ingredients"] or ingredient in pizza2["ingredients"]:
            return True
    return False

