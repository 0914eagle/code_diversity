
def solve(n, friends):
    # Initialize a dictionary to store the toppings and their counts
    toppings = {}

    # Iterate over the friends' lists of wishes
    for friend in friends:
        # Iterate over the friend's list of wishes
        for wish in friend:
            # If the wish is positive (i.e. the friend wants the topping), increment the count
            if wish.startswith("+"):
                toppings[wish[1:]] = toppings.get(wish[1:], 0) + 1
            # If the wish is negative (i.e. the friend does not want the topping), decrement the count
            elif wish.startswith("-"):
                toppings[wish[1:]] = toppings.get(wish[1:], 0) - 1

    # Initialize a list to store the selected toppings
    selected_toppings = []

    # Iterate over the toppings and their counts
    for topping, count in toppings.items():
        # If the count is greater than 0, add the topping to the list of selected toppings
        if count > 0:
            selected_toppings.append(topping)

    # Return the list of selected toppings
    return selected_toppings

