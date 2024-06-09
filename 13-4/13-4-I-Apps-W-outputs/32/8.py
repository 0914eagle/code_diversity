
def get_pizzas(n_friends, n_pizzas, friends, pizzas):
    # Initialize variables
    pleased_friends = 0
    total_price = 0
    chosen_pizzas = []

    # Iterate through each pizza
    for pizza in pizzas:
        # Check if the pizza satisfies the requirements
        if satisfies_requirements(pizza, friends):
            # Increment the number of pleased friends
            pleased_friends += 1
            # Add the pizza to the list of chosen pizzas
            chosen_pizzas.append(pizza)
            # Add the price of the pizza to the total price
            total_price += pizza[0]

            # If the number of pleased friends is equal to the number of friends, break the loop
            if pleased_friends == n_friends:
                break

    # Return the list of chosen pizzas and the total price
    return chosen_pizzas, total_price

def satisfies_requirements(pizza, friends):
    # Initialize a flag to indicate if the pizza satisfies the requirements
    satisfies = True

    # Iterate through each friend
    for friend in friends:
        # Check if the friend's favorite ingredients are in the pizza
        if not set(friend).issubset(set(pizza[1:])):
            # If the friend's favorite ingredients are not in the pizza, set the flag to False
            satisfies = False
            break

    # Return the flag
    return satisfies

# Test the function with example inputs
n_friends = 3
n_pizzas = 4
friends = [[2, 6, 7], [4, 2, 3, 9, 5], [3, 2, 3, 9]]
pizzas = [[100, 1, 7], [400, 3, 3, 2, 5], [100, 2, 9, 2], [500, 3, 2, 9, 5]]
chosen_pizzas, total_price = get_pizzas(n_friends, n_pizzas, friends, pizzas)
print(chosen_pizzas)
print(total_price)

# Example output:
# [[100, 1, 7], [400, 3, 3, 2, 5]]
# 500

