
def get_toppings(wishes):
    # Initialize a dictionary to count the number of wishes for each topping
    topping_counts = {}
    for wish in wishes:
        if wish.startswith("+"):
            topping = wish[1:]
            if topping not in topping_counts:
                topping_counts[topping] = 1
            else:
                topping_counts[topping] += 1

    # Sort the toppings by their count in descending order
    sorted_toppings = sorted(topping_counts.items(), key=lambda x: x[1], reverse=True)

    # Return the top 3 toppings with the highest count
    return [topping for topping, count in sorted_toppings[:3]]

