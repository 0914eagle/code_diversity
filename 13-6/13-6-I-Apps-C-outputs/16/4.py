
def get_toppings(n_friends, friend_wishes):
    # Initialize a dictionary to store the toppings and their counts
    topping_counts = {}

    # Iterate over the list of friend wishes
    for friend in friend_wishes:
        # Split the wish list into toppings and their counts
        toppings, counts = zip(*friend.split())

        # Update the topping counts for each topping in the wish list
        for topping, count in zip(toppings, counts):
            if topping not in topping_counts:
                topping_counts[topping] = 0
            topping_counts[topping] += int(count)

    # Sort the topping counts in descending order
    sorted_toppings = sorted(topping_counts.items(), key=lambda x: x[1], reverse=True)

    # Initialize the selected toppings list
    selected_toppings = []

    # Iterate over the sorted toppings and add them to the selected toppings list
    for topping, count in sorted_toppings:
        if count >= n_friends / 3:
            selected_toppings.append(topping)

    return selected_toppings

