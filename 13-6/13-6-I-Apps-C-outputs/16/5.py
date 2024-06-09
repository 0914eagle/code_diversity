
def get_toppings(n_friends, friends_wishes):
    # Initialize a dictionary to store the toppings and their counts
    toppings = {}

    # Loop through each friend's wishes and increment the count of each topping
    for friend in friends_wishes:
        for wish in friend:
            if wish[0] == "+":
                topping = wish[1:]
                if topping not in toppings:
                    toppings[topping] = 1
                else:
                    toppings[topping] += 1

    # Loop through the dictionary and select the toppings with the highest count
    selected_toppings = []
    for topping, count in toppings.items():
        if count >= n_friends / 3:
            selected_toppings.append(topping)

    return selected_toppings

