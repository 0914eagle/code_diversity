
def solve(n_friends, friends_wishes):
    # Initialize a dictionary to store the count of each topping
    topping_count = {}

    # Iterate over the list of friends and their wishes
    for friend in friends_wishes:
        # Split the friend's wishes into a list of toppings
        toppings = friend.split()

        # Iterate over the toppings and increment the count for each topping
        for topping in toppings:
            if topping not in topping_count:
                topping_count[topping] = 1
            else:
                topping_count[topping] += 1

    # Initialize a list to store the selected toppings
    selected_toppings = []

    # Iterate over the dictionary of topping counts and select the toppings with the highest count
    for topping, count in topping_count.items():
        if count >= n_friends / 3:
            selected_toppings.append(topping)

    # Return the list of selected toppings
    return selected_toppings

