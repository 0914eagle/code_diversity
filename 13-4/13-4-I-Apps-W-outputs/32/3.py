
def get_two_pizzas(n, m, friends, pizzas):
    # Initialize the maximum number of pleased friends to 0
    max_pleased_friends = 0
    # Initialize the indices of the two pizzas to be returned
    pizza1, pizza2 = 0, 0

    # Iterate over each pizza
    for i in range(m):
        # Initialize the number of pleased friends to 0
        pleased_friends = 0
        # Iterate over each friend
        for j in range(n):
            # Check if the friend's favorite ingredients are in the current pizza
            if set(friends[j]).issubset(set(pizzas[i])):
                # Increment the number of pleased friends
                pleased_friends += 1
        # Check if the current pizza pleases more friends than the previous pizzas
        if pleased_friends > max_pleased_friends:
            # Update the maximum number of pleased friends
            max_pleased_friends = pleased_friends
            # Update the indices of the two pizzas
            pizza1, pizza2 = i, (i+1)%m

    # Return the indices of the two pizzas
    return pizza1, pizza2

