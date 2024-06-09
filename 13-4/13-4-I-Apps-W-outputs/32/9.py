
def get_pizza_indices(n, m, friends, pizzas):
    # Initialize variables
    pleased_friends = 0
    total_price = 0
    pizza_indices = []

    # Iterate over each pizza
    for i in range(m):
        # Check if the pizza satisfies the requirements of at least one friend
        satisfied_friends = 0
        for friend in friends:
            if is_pizza_satisfying(friend, pizzas[i]):
                satisfied_friends += 1

        # If the pizza satisfies the requirements of at least one friend, add it to the list of pizzas
        if satisfied_friends > 0:
            pizza_indices.append(i)
            pleased_friends += satisfied_friends
            total_price += pizzas[i]["price"]

    # If there are multiple solutions, return the one with the lowest total price
    if len(pizza_indices) > 2:
        return sorted(pizza_indices, key=lambda x: pizzas[x]["price"])[:2]

    # Otherwise, return the list of pizza indices
    return pizza_indices

def is_pizza_satisfying(friend, pizza):
    # Check if the pizza contains at least one of the friend's favorite ingredients
    for ingredient in friend["favorite_ingredients"]:
        if ingredient in pizza["ingredients"]:
            return True
    return False

