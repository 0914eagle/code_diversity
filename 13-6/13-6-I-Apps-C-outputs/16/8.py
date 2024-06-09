
def get_pizza_toppings(n_friends, wishes):
    # Initialize a dictionary to store the toppings and their counts
    toppings = {}

    # Loop through each friend's wishes
    for friend in wishes:
        # Loop through each wish of the current friend
        for wish in friend:
            # If the wish is positive (i.e. +<topping>), increment the count for that topping
            if wish[0] == "+":
                toppings[wish[1:]] = toppings.get(wish[1:], 0) + 1
            # If the wish is negative (i.e. -<topping>), decrement the count for that topping
            else:
                toppings[wish[1:]] = toppings.get(wish[1:], 0) - 1

    # Initialize a list to store the selected toppings
    selected_toppings = []

    # Loop through the toppings and their counts
    for topping, count in toppings.items():
        # If the count is greater than 0, add the topping to the selected toppings list
        if count > 0:
            selected_toppings.append(topping)

    # Return the selected toppings list
    return selected_toppings

