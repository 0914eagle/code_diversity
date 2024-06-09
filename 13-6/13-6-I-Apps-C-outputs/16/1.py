
def get_toppings(num_friends, friends_wishes):
    # Initialize a dictionary to store the toppings and their counts
    toppings = {}

    # Iterate over the friends' wishes and increment the count of each topping
    for friend in friends_wishes:
        for wish in friend:
            if wish[0] == "+":
                topping = wish[1:]
                if topping not in toppings:
                    toppings[topping] = 1
                else:
                    toppings[topping] += 1

    # Sort the toppings by count in descending order
    sorted_toppings = sorted(toppings.items(), key=lambda x: x[1], reverse=True)

    # Return the top 3 toppings with the highest count
    return [topping for topping, count in sorted_toppings[:3]]

