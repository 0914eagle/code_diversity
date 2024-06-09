
def get_toppings(n_friends, friends_wishes):
    # Initialize a dictionary to count the number of wishes for each topping
    topping_counts = {}
    for friend in friends_wishes:
        for wish in friend:
            if wish.startswith("+"):
                topping = wish[1:]
                if topping not in topping_counts:
                    topping_counts[topping] = 1
                else:
                    topping_counts[topping] += 1
    
    # Sort the toppings by their count in descending order
    sorted_toppings = sorted(topping_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Create a list of toppings with at least 2/3 of their wishes fulfilled
    fulfilled_toppings = []
    for topping, count in sorted_toppings:
        if count >= n_friends / 3:
            fulfilled_toppings.append(topping)
    
    return fulfilled_toppings

