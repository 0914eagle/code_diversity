
def get_pizza_indices(n, m, friends, pizzas):
    # Initialize variables
    pleased_friends = 0
    total_price = 0
    pizza1 = 0
    pizza2 = 0

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
                if current_pleased_friends > pleased_friends or (current_pleased_friends == pleased_friends and total_price > pizzas[i]['price'] + pizzas[j]['price']):
                    pleased_friends = current_pleased_friends
                    total_price = pizzas[i]['price'] + pizzas[j]['price']
                    pizza1 = i
                    pizza2 = j

    # Return the indices of the two pizzas that please the maximum number of friends and have the minimum total price
    return pizza1, pizza2

# Check if a friend is pleased with a given combination of pizzas
def is_pleased(friend, pizza1, pizza2):
    for ingredient in friend['favorite_ingredients']:
        if ingredient not in pizza1['ingredients'] and ingredient not in pizza2['ingredients']:
            return False
    return True

